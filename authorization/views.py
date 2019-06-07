import json
import hashlib
import os
from plan.settings import IMAGES_DIR
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from utils.auth import c2s, already_authorized
from utils.response import ReturnCode, CommonResponseMixin
from .models import Yonghu, Renzheng
from utils.idcard import idcard_info
from utils.bizlicense import bizlicense_info

# Create your views here.
class UserView(View, CommonResponseMixin):
    def get(self, request):
        pass

    def post(self, request):
        return


def __authorization_by_code(request):
    data = request.body.decode("utf-8")
    data = json.loads(data)
    code = data.get('code').strip()
    appId = data.get('appId').strip()
    nickName = data.get('nickName').strip()

    response = {}
    if not code or not appId:
        response['message'] = '登陆失败，需要完整数据'
        response['code'] = ReturnCode.BROKEN_AUTHORIZED_DATA
        return JsonResponse(data=response, safe=False)

    data = c2s(appId, code)
    openid = data.get('openid')
    if not openid:
        response = CommonResponseMixin.wrap_json_response(code=ReturnCode.FAILED, message="auth failed.")
        return JsonResponse(data=response)

    request.session['open_id'] = openid
    request.session['is_authorized'] = True

    if not Yonghu.objects.filter(open_id=openid):
        user = Yonghu(open_id=openid, nickname=nickName)
        user.save()
    print("new user: openid: %s, nickName: %s" % (openid, nickName))

    response = CommonResponseMixin.wrap_json_response(code=ReturnCode.SUCCESS, message='auth success')
    return JsonResponse(data=response, safe=False)



def authorization(request):
    return __authorization_by_code(request)

def get_status(request):
    print('call get_status function...')
    if already_authorized(request):
        data = {"is_authorized": 1}
    else:
        data = {"is_authorized": 0}
    response = CommonResponseMixin.wrap_json_response(data=data, code=ReturnCode.SUCCESS)
    return JsonResponse(response, safe=False)

def logout(request):
    '''
    注销，小程序删除存储的Cookies
    '''
    request.session.clear()
    response = {}
    response['result_code'] = 0
    response['message'] = 'logout success.'
    return JsonResponse(response, safe=False)

# 接受身份验证图片
class UploadImage(View, CommonResponseMixin):
    def get(self, request):
        pass

    def post(self, request):
        print('上传')
        files = request.FILES
        shuju = []

        # 三个图片循环三次
        for key, value in files.items():
            content = value.read()
            md5 = hashlib.md5(content).hexdigest()
            path = os.path.join(IMAGES_DIR + '/', md5 + '.jpg')
            with open(path, 'wb') as f:
                f.write(content)
            yonghu = key[:-1]
            yonghu = Yonghu.objects.get(nickname=yonghu)
            # 如果已经存在这个renzheng，那就直接在上面修改
            if Renzheng.objects.get(yonghu=yonghu):
                renzheng = Renzheng.objects.get(yonghu=yonghu)
            # 如果不存在，就创建一个新的
            else:
                renzheng = Renzheng()
                renzheng.yonghu = yonghu
            if key[-1] == '0':
                renzheng.ID_zheng = md5 + '.jpg'
                image_list = ['https://api.gaoblog.cn/api/v1.0/server/image?md5=' + md5 ]
                face = 0
                data = idcard_info(image_list=image_list, face=face)
                try:
                    renzheng.name = data['name']
                    renzheng.sex = data['sex']
                    renzheng.nationality = data['nation']
                    renzheng.birth = data['birth']
                    renzheng.address = data['address']
                    renzheng.id_num = data['id']
                except Exception:
                    renzheng.status = '审核失败'
            elif key[-1] == '1':
                renzheng.ID_fan = md5 + '.jpg'
                image_list = ['https://api.gaoblog.cn/api/v1.0/server/image?md5=' + md5 ]
                face = 1
                data = idcard_info(image_list=image_list, face=face)
                try:
                    renzheng.issue = data['issue']
                    renzheng.start_date = data['start_date']
                    renzheng.end_date = data['end_date']
                except Exception:
                    renzheng.status = '审核失败'
            else:
                renzheng.Ying = md5 + '.jpg'
                image_list = 'https://api.gaoblog.cn/api/v1.0/server/image?md5=' + md5
                data = bizlicense_info(image_list)
                try:
                    renzheng.zhuce_num = data['注册号']
                    renzheng.fading_daibiao = data['法定代表人']
                    renzheng.compuny = data['公司名称']
                    renzheng.cp_address = data['地址']
                    renzheng.cp_data = data['营业期限']
                except Exception:
                    renzheng.status = '审核失败'
            renzheng.save()
        shuju.append({'status': renzheng.status})
        data = self.wrap_json_response(data=shuju, code=ReturnCode.SUCCESS, message='upload image success.')
        return JsonResponse(data=data, safe=False)


# 获取认证审核状态
class Status(View, CommonResponseMixin):
    def get(self, request):
        pass

    def post(self, request):
        data = request.body.decode('utf-8')
        data = json.loads(data)
        nickname = data['nickName']
        yonghu = Yonghu.objects.get(nickname=nickname)
        print(hasattr(yonghu, 'renzheng'))
        if hasattr(yonghu, 'renzheng'):
            status = yonghu.renzheng.status
        else:
            status = '不存在'
        data = {}
        data['status'] = status
        print(data)
        data = self.wrap_json_response(data=data, code=ReturnCode.SUCCESS, message='success.')
        return JsonResponse(data=data, safe=False)