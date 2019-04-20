"托管机构、图片、小孩 模型类"


from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# 托管机构
class Shangjia(models.Model):
    # 名称
    name = models.CharField(max_length=256, unique=True, verbose_name='商户名称')
    # 商家评分
    score = models.FloatField(default=5.0, verbose_name='商家评分')
    # 是否实时监控
    is_real_time_monitoring = models.BooleanField(default=False, verbose_name='实时监控')
    # 是否购买保险
    is_purchase_insurance = models.BooleanField(default=False, verbose_name='购买保险')
    # 是否已经实名认证
    is_Verified = models.BooleanField(default=False, verbose_name='实名认证')
    # 学历认证
    is_academic_certificate = models.BooleanField(default=False, verbose_name='学历认证')
    # 健康认证
    is_Health_certification = models.BooleanField(default=False, verbose_name='健康认证')
    # 商家介绍
    introduction = models.CharField(max_length=256, verbose_name='商家介绍')
    # 商家省份
    province = models.CharField(max_length=256, null=True, verbose_name='所在省份')
    # 商家城市
    city = models.CharField(max_length=256, null=True, verbose_name='所在城市')
    # 商家具体地址
    location = models.CharField(max_length=255, null=True, verbose_name='商家地址')
    # 商家所在地理位置
    latitude = models.FloatField(verbose_name="用户所在纬度", null=True)
    longitude = models.FloatField(verbose_name="用户所在经度", null=True)

    def distance(self, latitude, longitude):
        from evaluation.solve.find_job import zuijin
        return zuijin(self.latitude, self.longitude, latitude, longitude)

    def __str__(self):
        return self.name


# 项目所有的图片
class Image(models.Model):
    # 图片
    image = models.ImageField(verbose_name='图片', upload_to='photos/%Y/%m/%d/')
    # 通用外键
    content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')



# 小孩
class Child(models.Model):
    # 出生姓名
    name = models.CharField(max_length=32, verbose_name='姓名')
    # 出生日期
    born_date = models.DateField(verbose_name='出生日期', blank=True)
    # 性别选项
    GENDER = (
        ('boy', '男孩'),
        ('girl', '女孩')
    )
    gender = models.CharField(choices=GENDER, verbose_name='性别', blank=True, max_length=12)
    # 年级选项
    GRADE = (
        ('BS', '未上学'),
        ('KSSC', '幼儿园小小班'),
        ('KSC', '幼儿园小班'),
        ('KMC', '幼儿园中班'),
        ('KC', '幼儿园大班'),
        ('GO', '一年级'),
        ('GT', '二年级'),
        ('GTH', '三年级'),
        ('GF', '四年级'),
        ('GFI', '五年级'),
        ('GS', '六年级'),
        ('GSE', '初一'),
        ('GE', '初二'),
        ('GN', '初三'),
        ('HO', '高一'),
        ('HT', '高二'),
        ('HTW', '高三')
    )
    # 年级
    grade = models.CharField(choices=GRADE, verbose_name='年级', blank=True, max_length=12)
    # 备用联系人
    another_contact_name = models.CharField(max_length=32, blank=True, verbose_name='备用联系人')
    # 备用联系电话
    another_contact_phonenumber = models.CharField(max_length=11, verbose_name='备用联系电话', blank=True)
    # 是否有过敏史
    is_allergy = models.BooleanField(default=False, verbose_name='是否有过敏史')
    # 过敏史
    allergy = models.TextField(verbose_name='过敏史', blank=True)
    # 通用外键——用户、商家、订单
    content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.name