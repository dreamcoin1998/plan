from django.contrib import admin
from .models import Order, Recruitment, Grade

# Register your models here.
class RecruitmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'work_location', 'academic', 'subject', 'price', 'type', 'user', 'shangjia')
    ordering = ('id',)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'server_type', 'charging_method', 'time_num', 'price', 'admission_time', 'is_payment', 'shangjia', 'user', 'phone')
    ordering = ('id',)


class GradeAdmin(admin.ModelAdmin):
    list_display = ('id', 'grade', 'order')
    ordering = ('id',)

admin.site.register(Recruitment)
admin.site.register(Order)
admin.site.register(Grade)