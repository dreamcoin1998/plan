from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('server/', include('api.urls')),
    path('auth/', include('authorization.urls'))
]