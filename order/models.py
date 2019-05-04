"招聘信息、订单类型模型类"
from django.contrib.contenttypes.models import ContentType
from django.db import models
from api.models import Shangjia, Image
from authorization.models import Yonghu
from django.db.models.fields import exceptions

class tupian():
    def image(self):
        try:
            ct = ContentType.objects.get_for_model(self)
            image = Image.objects.get(content_type=ct, object_id=self.pk)
            return image.url
        except exceptions.ObjectDoesNotExist:
            return 0

# 招聘信息
class Recruitment(models.Model, tupian):
    # 工作职位
    position = models.CharField(max_length=50, verbose_name='职位', null=True)
    # 工作描述
    description = models.CharField(max_length=256, verbose_name='工作描述', null=True)
    # 工作地点
    work_location = models.CharField(max_length=256, verbose_name='工作地点')
    # 需求人数
    peo_num = models.PositiveIntegerField(default=100, verbose_name='人数')
    # 学历要求
    ACADEMIC = (
        ('Dazhuan', '大专'),
        ('Benke', '本科')
    )
    academic = models.CharField(max_length=20, choices=ACADEMIC, default='Dazhuan', verbose_name='学历要求')
    # 科目要求
    SUBJECT = (
        ('Chinese', '语文'),
        ('Math', '数学'),
        ('English', '英语'),
        ('Biological', '生物'),
        ('Physical', '物理'),
        ('Chemistry', '化学'),
        ('History', '历史'),
        ('Geography', '地理'),
        ('Political', '政治')
    )
    subject = models.CharField(max_length=20, choices=SUBJECT, default="Chinese")
    # 结算方式
    PAY_METHOD = (
        ('Day', '日结'),
        ('Week', '周结'),
        ('Month', '月结'),
        ('Term', '学期')
    )
    pay_method = models.CharField(max_length=5, choices=PAY_METHOD, default='Month', verbose_name='结算方式')
    # 薪酬
    price = models.PositiveIntegerField(verbose_name='月薪')
    # 工作类型
    TYPE = (
        ('Full_Time', '全职'),
        ('Part_Time', '兼职')
    )
    type = models.CharField(max_length=20, choices=TYPE, default='工作类型')
    # 求职者——用户
    user = models.ManyToManyField(Yonghu, blank=True)
    # 托管平台
    shangjia = models.ForeignKey(Shangjia, on_delete=models.DO_NOTHING)
    # 招聘信息 创建时间
    pub_time = models.DateTimeField(auto_now_add=True, null=True)
    # 招聘是否结束
    is_stop = models.BooleanField(verbose_name='是否结束', default=False)

    def __str__(self):
        return str(self.pk)



# 订单类型
class Order(models.Model):
    # 服务类型
    SERVER_TYPE = (
        ('Child_care', '孩子看护'),
        ('After-school tutoring', '课后辅导'),
        ('Interest_development', '兴趣培养')
    )
    server_type = models.CharField(max_length=50, choices=SERVER_TYPE, default='Child_care', verbose_name='服务类型')
    # 收费方式
    CHARGING_METHOD = (
        ('Per_Hour', '每小时'),
        ('Per_Day', '每天'),
        ('Per_Month', '每月'),
        ('Per_Semester', '每学期'),
        ('Per_Quarter', '每季度')
    )
    charging_method = models.CharField(max_length=20, choices=CHARGING_METHOD, default='Per_Month', verbose_name='收费方式')
    # 托管时间——单位是上面的收费方式
    time_num = models.PositiveIntegerField(verbose_name='托管时间')
    # 收费金额——单位为上面的收费方式
    price = models.PositiveIntegerField(verbose_name='收费金额')
    # 入学时间
    admission_time = models.DateField(verbose_name='入学时间')
    # 订单状态——未付款、待评价、已完成
    status = models.CharField(max_length=128, default='未付款')
    # 商家
    shangjia = models.ForeignKey(Shangjia, on_delete=models.DO_NOTHING, verbose_name='所属商家')
    # 用户
    user = models.ForeignKey(Yonghu, on_delete=models.DO_NOTHING, verbose_name='所属用户')
    # 用户的电话号码
    phone = models.CharField(max_length=11, blank=True, verbose_name='联系电话')
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True, null=True)


# 招生对象年级
class Grade(models.Model):
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
    grade = models.CharField(max_length=5, choices=GRADE, verbose_name='年级', blank=True)
    # 订单类型
    order = models.ForeignKey(Order, on_delete=models.DO_NOTHING, related_name='order')