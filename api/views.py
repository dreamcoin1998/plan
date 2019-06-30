import os
import re
import json
import hashlib
from django.shortcuts import render
from plan import settings
from utils.response import CommonResponseMixin, ReturnCode
from django.views import View
from django.http import JsonResponse, FileResponse
from .models import Child, Image, Shangjia
from authorization.models import Yonghu
from django.contrib.contenttypes.models import ContentType
from plan.settings import IMAGES_DIR
from order.models import Recruitment
from django.db.models import Q
from utils.auth import c2s


# 处理用户返回的地理位置,后期进行一些推荐商家，筛选等等处理
class user_location(View, CommonResponseMixin):
    def get(self, request):
        pass

    def post(self, request):
        data = request.body.decode("utf-8")
        data = eval(data)
        print(data)
        response = self.wrap_json_response(code=ReturnCode.FAILED, message="auth failed.")
        return JsonResponse(data=response)


# 向前端传送图片
class ImageView(View, CommonResponseMixin):
    def get(self, request):
        # 获取请求图片文件名
        md5 = request.GET.get('md5')
        # 获取请求图片完整路径
        imgfile = os.path.join(settings.IMAGES_DIR, md5 + '.jpg')
        print(imgfile)
        # 如果文件存在
        if os.path.exists(imgfile):
            data = open(imgfile, 'rb').read()
            # return HttpResponse(data, content_type='image/jpg')
            return FileResponse(open(imgfile, 'rb'), content_type='image/jpg')
        else:
            response = self.wrap_json_response(code=ReturnCode.RESOURCE_NOT_FOUND, message='file is not exists.')
            return JsonResponse(data=response, safe=False)


class JobView(View, CommonResponseMixin):
    def get(self, request):
        # 获取请求图片文件名
        md5 = request.GET.get('md5')
        # 获取请求图片完整路径
        imgfile = os.path.join(settings.MEDIA_ROOT, md5)
        print(imgfile)
        # 如果文件存在
        if os.path.exists(imgfile):
            # return HttpResponse(data, content_type='image/jpg')
            return FileResponse(open(imgfile, 'rb'), content_type='image/jpg')
        else:
            response = self.wrap_json_response(code=ReturnCode.RESOURCE_NOT_FOUND, message='file is not exists.')
            return JsonResponse(data=response, safe=False)


class JobDetails(View, CommonResponseMixin):
    def get(self, request):
        pass


# 获取前端传过来的小孩信息
class Baby(View, CommonResponseMixin):
    def get(self, request):
        pass

    def post(self, request):
        data = request.body.decode('utf-8')
        print(data)
        data = json.loads(data)
        print(data)
        action = data['action']
        if action == 'add':
            baby = Child()
            print('执行添加')
        else:
            baby = Child.objects.get(id=data['id'])
            print('执行修改')
        baby.name = data['name']
        baby.born_date = data['date']
        if data['sex'] == '男':
            baby.gender = 'boy'
        elif data['sex'] == '女':
            baby.gender = 'girl'
        if data['grade'] is not None:
            index = int(data['grade'])
            baby.grade = Child.GRADE[index][1]
        baby.contact_name = data['connect_man']
        baby.contact_phone = data['connect_phone']
        baby.another_contact_name = data['by_connect_man']
        baby.another_contact_phonenumber = data['by_connect_phone']
        if data['guomin'] == '有':
            baby.is_allergy = True
        else:
            baby.is_allergy = False
        baby.allergy = data['guomin_history']
        baby.image = data['touxiang']
        baby.card_type = data['card_type']
        baby.idcard = data['idcard']
        baby.school = data['school']
        baby.school_area = data['school_area']
        yonghu = Yonghu.objects.get(open_id=c2s(data['appid'], data['code'])['openid'])
        yh = ContentType.objects.get_for_model(Yonghu)
        baby.content_type = yh
        baby.object_id = yonghu.id
        baby.save()
        response = self.wrap_json_response(code=ReturnCode.SUCCESS, message='baby success.')
        return JsonResponse(data=response, safe=False)


# 上传图片类
class uploadImage(View, CommonResponseMixin):
    def get(self, request):
        pass

    def post(self, request):
        file = request.FILES
        print(file)
        data = []
        for key, value in file.items():
            content = value.read()
            md5 = hashlib.md5(content).hexdigest()
            path = os.path.join(IMAGES_DIR + '/', md5 + '.jpg')
            with open(path, 'wb') as f:
                f.write(content)
            data.append({'name': key, 'md5': md5})
        data = self.wrap_json_response(data=data, code=ReturnCode.SUCCESS, message='upload success.')
        return JsonResponse(data=data, safe=False)


# 获取用户所填写的小孩信息
class getChild(View, CommonResponseMixin):
    def get(self, request):
        code = request.GET.get('code')
        appId = request.GET.get('appId')
        open_id = c2s(appId, code)['openid']
        yonghu = Yonghu.objects.get(open_id=open_id)
        child = yonghu.child.all()
        data = []
        for ch in child:
            baby = {}
            baby['id'] = ch.id
            baby['name'] = ch.name
            baby['date'] = ch.born_date
            baby['sex'] = ch.gender
            baby['grade'] = ch.grade
            baby['connect_man'] = ch.contact_name
            baby['connect_phone'] = ch.contact_phone
            baby['by_connect_man'] = ch.another_contact_name
            baby['by_connect_phone'] = ch.another_contact_phonenumber
            if ch.is_allergy == True:
                baby['guomin'] = '有'
            else:
                baby['guomin'] = '无'
            baby['allergy'] = ch.allergy
            baby['touxiang'] = ch.image
            baby['card_type'] = ch.card_type
            baby['idcard'] = ch.idcard
            baby['school'] = ch.school
            school_area = []
            liebiao = re.match(r"\['(\w+)', '(\w+)', '(\w+)'\]", ch.school_area).groups()
            for n in liebiao:
                school_area.append(n)
            print(school_area)
            baby['school_area'] = school_area
            data.append(baby)
        print(data)
        data = self.wrap_json_response(data=data, code=ReturnCode.SUCCESS, message='child success.')
        return JsonResponse(data=data, safe=False)


# 删除小孩信息
class deleteChild(View, CommonResponseMixin):
    def get(self, request):
        pass

    def post(self, request):
        data = request.body.decode('utf-8')
        print(data)
        data = json.loads(data)
        print(data)
        id = data['id']
        child = Child.objects.get(id=id)
        child.delete()
        print('删除成功！')
        return JsonResponse(data=self.wrap_json_response(code=ReturnCode.SUCCESS, message='delete success.'), safe=False)


'''
实现用户搜索功能，搜索商家信息和招聘信息
'''
class search(View, CommonResponseMixin):
    def get(self, request):
        pass

    def post(self, request):
        data = request.body.decode('utf-8')
        data = json.loads(data)
        inquiry = data['q'] # 获取前端查询词
        # 根据查询词在Shangjia进行不分大小写的查找
        shangjias = Shangjia.objects.filter(name__icontains=inquiry)
        print(shangjias)
        # 根据查询词在Recruitment的position或description字段进行不区分大小写的查找
        recruitments = Recruitment.objects.filter(Q(position__icontains=inquiry) | Q(description__icontains=inquiry))
        print(recruitments)
        print(recruitments!=[])
        data = []
        # 如果查询到的商家信息不为空
        if len(shangjias) > 0:
            print('执行1')
            for shangjia in shangjias:
                shuju = {}
                for key, value in shangjia.__dict__.items():
                    shuju[key] = value
                shuju.pop('_state')
                shuju['distance'] = shangjia.distance(shangjia.latitude, shangjia.longitude)
                shuju['type'] = 'shangjia'
                data.append(shuju)
        elif len(recruitments) > 0:
            print('执行')
            for recruitment in recruitments:
                print(recruitment)
                shuju = {}
                for key, value in recruitment.__dict__.items():
                    shuju[key] = value
                shuju.pop('_state')
                shuju['type'] = 'recruitment'
                data.append(shuju)
        data = self.wrap_json_response(data=data, code=ReturnCode.SUCCESS, message='inquiry success.')
        print(data)
        return JsonResponse(data=data, safe=False)
