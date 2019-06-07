from django.contrib import admin
from .models import Yonghu, Renzheng

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','open_id', 'nickname')
    ordering = ('id',)


class RenzhengAdmin(admin.ModelAdmin):
    list_display = ('name', 'nationality', 'id_num', 'sex', 'start_date', 'end_date', 'status')
    ordering = ('id',)


admin.site.register(Yonghu)
admin.site.register(Renzheng)