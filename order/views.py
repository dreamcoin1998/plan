from django.views import View
from utils.response import CommonResponseMixin, ReturnCode
from django.http import JsonResponse
from api.models import Shangjia
from evaluation.solve.find_job import zuijin


# 处理小程序 招聘信息页 的筛选函数
class send_job(View, CommonResponseMixin):
    def get(self, request):
        pass

    def post(self, request):
        zidian = {}
        liebiao1 = []
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
            for n in data: # 遍历排序结果
                list1 = n[0].recruitment_set.all() # 获取排序结果中的recruitment对象
                # print(list1)
                # print(liebiao1)
                for i in list1: # 遍历recruitment，获取他们recruitment的属性并装配成字典
                    # 将获取到的招聘订单装配成dict
                    duixiang = {}
                    duixiang['position'] = i.position
                    duixiang['description'] = i.description
                    duixiang['work_location'] = i.work_location
                    duixiang['academic'] = i.academic
                    duixiang['subject'] = i.subject
                    duixiang['price'] = i.price
                    duixiang['type'] = i.type
                    duixiang['pub_time'] = i.pub_time
                    duixiang['shangjia'] = n[0].name
                    liebiao1.append(duixiang) # 将带有recruitment属性的字典全部装配进列表中
            data = self.wrap_json_response(data=liebiao1, code=ReturnCode.SUCCESS, message='success.')
            return JsonResponse(data, safe=False)





        # 发送用户请求的数据
        response = self.wrap_json_response(code=ReturnCode.SUCCESS, message='fail.')
        return JsonResponse(data=response)