from django.views import View
from utils.response import CommonResponseMixin, ReturnCode
from django.http import JsonResponse
from api.models import Shangjia, Image
from evaluation.solve.find_job import get_xinxi, pingfen, chengshi, pay_chinese
from .models import Recruitment
from django.contrib.contenttypes.models import ContentType
from authorization.models import Yonghu

# 排序算法获取所需数据
def get_sort(shuju):
    data = []
    image = ContentType.objects.get_for_model(Recruitment)
    for i in shuju:
        duixiang = {}
        duixiang['id'] = i[0].id
        duixiang['position'] = i[0].position
        duixiang['description'] = i[0].description
        duixiang['work_location'] = i[0].work_location
        duixiang['renshu'] = i[0].peo_num
        duixiang['academic'] = i[0].academic
        duixiang['subject'] = i[0].subject
        duixiang['price'] = str(i[0].price) + pay_chinese(i[0].pay_method)
        duixiang['type'] = i[0].type
        duixiang['pub_time'] = i[0].pub_time.strftime("%Y-%m-%d")
        duixiang['shangjia'] = i[0].shangjia.name
        duixiang['address'] = i[0].shangjia.province + i[0].shangjia.city + i[0].shangjia.location
        try:
            tupian = []
            tp_duixiang = Image.objects.filter(content_type=image, object_id=i.id)
            for i in tp_duixiang:
                tupian.append(i.image.url)
            duixiang['image'] = tupian
        except:
            duixiang['image'] = ''
        data.append(duixiang)
    return data

# 处理小程序 招聘信息页 的筛选函数
class send_job(View, CommonResponseMixin):
    def get(self, request):
        data = []
        zidian = {}
        sort = request.GET.get('sort')
        if request.GET.get('value') is not None:
            value = request.GET.get('value')
            print(value)
        city = request.GET.get('city')
        print('城市：', city)
        # 如果是综合排序
        if sort == 'zhonghe':
            # 获取本城市所有的商家
            shangjia = Shangjia.objects.filter(city=city)
            for sj in shangjia:
                re = sj.recruitment_set.all() # 获取所有的招聘信息
                for i in re:
                # 定义字典，方便排序
                    zidian[i] = i.price
            # 按降序排列
            if value == 'down':
                shuju = sorted(zidian.items(), key=lambda x: x[1], reverse=True)
                data = get_sort(shuju)

            # 按升序排列
            elif value == 'up':
                shuju = sorted(zidian.items(), key=lambda x: x[1])
                data = get_sort(shuju)
            data = self.wrap_json_response(data=data, code=ReturnCode.SUCCESS, message='pailie success.')
            return JsonResponse(data, safe=False)
        elif sort == 'city':
            data = chengshi(city)
            data = self.wrap_json_response(data=data, code=ReturnCode.SUCCESS, message='chengshi success.')
            return JsonResponse(data, safe=False)

    def post(self, request):
        zidian = {}
        # 接收用户的请求信息并解析用户请求
        print(request.body, '成功接受请求')
        data = request.body.decode("utf-8")
        print(data, '成功解码')
        data = eval(data)
        print(data, '成功')
        # 根据用户请求响应用户的请求内容
        # 智能排序
        if data.get('sort') == 'intelligent':
            pass

        # 距离最近
        if data.get('sort') == 'near':
            latitude = data.get('latitude')
            longitude = data.get('longitude')
            city = data.get('city')
            print('城市：', city)
            for n in Shangjia.objects.filter(city=city): # 筛选出所在城市Shangjia
                num = n.distance(latitude, longitude) # 获取Shangjia对象所有的distence
                zidian[n] = num # 装配成字典
            data = sorted(zidian.items(), key=lambda x: x[1]) # 将字典按距离排序
            print(data)
            data = get_xinxi(data) # 获取商家对应的招聘信息
            print('距离最近', data)
            data = self.wrap_json_response(data=data, code=ReturnCode.SUCCESS, message='distence success.')
            return JsonResponse(data, safe=False)

        # 根据评分优先排序
        elif data.get('sort') == 'praise':
            city = data.get('city') # 获取所在城市信息
            print(city)
            data = pingfen(city)
            data = self.wrap_json_response(data=data, code=ReturnCode.SUCCESS, message='pingfen success.')
            return JsonResponse(data, safe=False)

        # 根据选择地区排序
        elif data.get('sort') == 'city':
            city = data.get('city')
            print(city)
            data = chengshi(city)
            data = self.wrap_json_response(data=data, code=ReturnCode.SUCCESS, message='chengshi success.')
            return JsonResponse(data, safe=False)

        # 用户自定义选项
        elif data.get('sort') == 'filter':
            if data.get('education'):
                education = data.get('education').split(' ') # 获取学历要求列表
            if data.get('subject'):
                subject = data.get('subject').split(' ') # 获取学科要求列表
            if data.get('salary'):
                salary = int(data.get('salary')) # 获取薪水范围
            if data.get('type'):
                type = data.get('type').split(' ') # 获取工作类型
            recruitment = Recruitment.objects.all()
            anxueli = []
            # 按照学历要求筛选
            if data.get('education') is not None: # 如果用户选择学历筛选项
                for xueli in education:
                    recruitment = recruitment.filter(academic=xueli)
                    anxueli += recruitment

            # 按照学科要求列表筛选
            anxueke = []
            if data.get('subject') is not None:
                # 循环筛选所选学科
                for xueke in subject:
                    recruitment = recruitment.filter(subject=xueke)
                    anxueke += recruitment

            # 按照薪水范围筛选
            anxinshui = []
            if data.get('salary') is not None:
                if salary == 1:
                    recruitment = recruitment.filter(price__lte=800) # 筛选薪酬小于等于800
                elif salary == 2:
                    recruitment = recruitment.filter(price__gt=800, price__lte=1500) # 800-1500
                elif salary == 3:
                    recruitment = recruitment.filter(price__gt=1500, price__lte=3000) # 1500-3000
                elif salary == 4:
                    recruitment = recruitment.filter(price__gt=3000, price__lte=5000) # 3000-5000
                elif salary == 5:
                    recruitment = recruitment.filter(price__gt=5000, price__lte=10000) # 5000-10000
                else:
                    recruitment = recruitment.filter(price__gt=10000) # 10000以上
                anxinshui += recruitment

            # 按照工作类型查找
            antype = []
            if data.get('type') is not None:
                for leixing in type:
                    recruitment = recruitment.filter(type=leixing)
                antype += recruitment
            recruitment = set(anxueli if anxueli else Recruitment.objects.all()) & set(anxueke if anxueke else Recruitment.objects.all()) & set(anxinshui if anxinshui else Recruitment.objects.all()) & set(antype if antype else Recruitment.objects.all())
            data = []
            image = ContentType.objects.get_for_model(Recruitment)
            for i in recruitment:
                duixiang = {}
                duixiang['id'] = i.id
                duixiang['position'] = i.position
                duixiang['description'] = i.description
                duixiang['work_location'] = i.work_location
                duixiang['renshu'] = i.peo_num
                duixiang['academic'] = i.academic
                duixiang['subject'] = i.subject
                duixiang['price'] = str(i.price) + pay_chinese(i.pay_method)
                duixiang['type'] = i.type
                duixiang['pub_time'] = i.pub_time.strftime("%Y-%m-%d")
                duixiang['shangjia'] = i.shangjia.name
                duixiang['address'] = i.shangjia.province + i.shangjia.city + i.shangjia.location
                try:
                    tupian = []
                    tp_duixiang = Image.objects.filter(content_type=image, object_id=i.id)
                    for i in tp_duixiang:
                        tupian.append(i.image.url)
                    duixiang['image'] = tupian
                except:
                    duixiang['image'] = ''
                data.append(duixiang)
            data = self.wrap_json_response(data=data, code=ReturnCode.SUCCESS, message='zidingyi success.')
            return JsonResponse(data, safe=False)

        # 发送用户请求的数据
        response = self.wrap_json_response(code=ReturnCode.SUCCESS, message='fail.')
        return JsonResponse(data=response)


# 招聘信息详情页获取商家信息
class GetXinxi(View, CommonResponseMixin):
    def get(self, request):
        pass

    def post(self, request):
        data = request.body.decode("utf-8")
        data = eval(data)

        xinxi_id = data.get('xinxi_id')
        recruitment = Recruitment.objects.get(id=xinxi_id)
        shangjia = recruitment.shangjia

        duixiang = {}
        duixiang['name'] = shangjia.name
        duixiang['introduction'] = shangjia.introduction
        duixiang['address'] = shangjia.province + shangjia.city + shangjia.location
        duixiang['id'] = shangjia.id

        data = self.wrap_json_response(data=duixiang, code=ReturnCode.SUCCESS, message='shangjia success.')
        return JsonResponse(data, safe=False)


# 用户点击申请
class apply(View, CommonResponseMixin):
    def get(self, request):
        pass

    def post(self, request):
        data = request.body.decode('utf-8')
        data = eval(data)
        print(data)
        try:
            id = data['id']
            nickname = data['nickname']
            re = Recruitment.objects.get(id=id) # 获取相应的Recruitment对象
            yonghu = Yonghu.objects.get(nickname=nickname)
            re.user.add(yonghu)
            re.save()
            data = self.wrap_json_response(code=ReturnCode.SUCCESS, message='apply success.')
        except Exception as e:
            print(e)
            data = self.wrap_json_response(code=ReturnCode.FAILED, message='apply failed.')
        return JsonResponse(data=data, safe=False)