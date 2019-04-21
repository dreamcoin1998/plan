from django.views import View
from utils.response import CommonResponseMixin, ReturnCode
from django.http import JsonResponse
from api.models import Shangjia
from evaluation.solve.find_job import get_xinxi, pingfen, chengshi
from .models import Recruitment


# 处理小程序 招聘信息页 的筛选函数
class send_job(View, CommonResponseMixin):
    def get(self, request):
        pass

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
            for n in Shangjia.objects.filter(city=city): # 筛选出所在城市Shangjia
                num = n.distance(latitude, longitude) # 获取Shangjia对象所有的distence
                zidian[n] = num # 装配成字典
            data = sorted(zidian.items(), key=lambda x: x[1]) # 将字典按距离排序
            zidian.clear() # 清除字典
            data = get_xinxi(data) # 获取商家对应的招聘信息
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
            education = data.get('education').split(' ') # 获取学历要求列表
            subject = data.get('subject').split(' ') # 获取学科要求列表
            salary = int(data.get('salary')) # 获取薪水范围
            type = data.get('type').split(' ') # 获取工作类型
            print(education, subject, salary, type)

            recruitment = Recruitment.objects.all()
            # 按照学历要求筛选
            if education is not None: # 如果用户选择学历筛选项
                for xueli in education:
                    recruitment = recruitment.filter(academic=xueli)

            # 按照学科要求列表筛选
            if subject is not None:
                # 循环筛选所选学科
                for xueke in subject:
                    recruitment = recruitment.filter(subject=xueke)

            # 按照薪水范围筛选
            if salary is not None:
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

            # 按照工作类型查找
            if type is not None:
                for leixing in type:
                    recruitment = recruitment.filter(type=leixing)

            data = []
            for i in recruitment:
                duixiang = {}
                duixiang['position'] = i.position
                duixiang['description'] = i.description
                duixiang['work_location'] = i.work_location
                duixiang['academic'] = i.academic
                duixiang['subject'] = i.subject
                duixiang['price'] = i.price
                duixiang['type'] = i.type
                duixiang['pub_time'] = i.pub_time
                duixiang['shangjia'] = i.shangjia.name
                data.append(duixiang)
            data = self.wrap_json_response(data=data, code=ReturnCode.SUCCESS, message='zidingyi success.')
            return JsonResponse(data, safe=False)

        # 发送用户请求的数据
        response = self.wrap_json_response(code=ReturnCode.SUCCESS, message='fail.')
        return JsonResponse(data=response)