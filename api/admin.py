from django.contrib import admin
from .models import Shangjia, Image, Child
# Register your models here.

class ShangjiaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location', 'is_real_time_monitoring', 'is_purchase_insurance', 'is_Verified', 'is_academic_certificate', 'is_Health_certification', 'province', 'city', 'score')
    ordering = ('id',)


class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'content_type', 'object_id', 'content_object')
    ordering = ('id',)


class ChildAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'born_date', 'gender', 'grade', 'another_contact_name', 'another_contact_phonenumber', 'is_allergy', 'allergy', 'content_type', 'object_id', 'content_object')
    ordering = ('id',)


admin.site.register(Shangjia, ShangjiaAdmin)
admin.site.register(Image)
admin.site.register(Child)