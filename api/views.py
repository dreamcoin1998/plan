from django.shortcuts import render
from utils.response import CommonResponseMixin, ReturnCode
from django.views import View
from django.http import JsonResponse

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