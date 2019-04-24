import os

from django.shortcuts import render

from plan import settings
from utils.response import CommonResponseMixin, ReturnCode
from django.views import View
from django.http import JsonResponse, FileResponse


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