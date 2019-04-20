from django.contrib import admin
from .models import Yonghu

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','open_id', 'nickname')
    ordering = ('id',)


admin.site.register(Yonghu)