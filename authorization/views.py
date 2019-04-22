import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from utils.auth import c2s, already_authorized
from utils.response import ReturnCode, CommonResponseMixin
from .models import Yonghu

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

