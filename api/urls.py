from django.urls import path, include
from .views import user_location, ImageView, JobView, Baby, uploadImage, getChild, deleteChild
from authorization.views import UserView, authorization
from order.views import send_job, GetXinxi
from evaluation.solve.find_order import Tuoguan, Tuoguan_shouye

urlpatterns = [
    path('auth', authorization),
    path('location', user_location.as_view()),
    path('getjob', send_job.as_view()),
    path('image', ImageView.as_view()),
    path('job', JobView.as_view()),
    path('shangjia', GetXinxi.as_view()),
    path('tuoguan', Tuoguan.as_view()),
    path('shouye', Tuoguan_shouye.as_view()),
    path('baby', Baby.as_view()),
    path('upload', uploadImage.as_view()),
    path('getchild', getChild.as_view()),
    path('delete', deleteChild.as_view())
]