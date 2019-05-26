from django.urls import path, include
from authorization.views import authorization, logout, UploadImage, Status
from utils.auth import already_authorized

urlpatterns = [
    path('login', authorization),
    path('yanzheng', already_authorized),
    path('logout', logout),
    path('image', UploadImage.as_view()),
    path('status', Status.as_view())
]