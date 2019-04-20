from django.urls import path, include
from .views import user_location
from authorization.views import UserView, authorization
from order.views import send_job

urlpatterns = [
    path('auth', authorization),
    path('location', user_location.as_view()),
    path('getjob', send_job.as_view())
]