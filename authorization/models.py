from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from api.models import Child

# 用户模型
class Yonghu(models.Model):
    # open_id
    open_id = models.CharField(max_length=64, unique=True)
    # 昵称
    nickname = models.CharField(max_length=256)
    # 小孩信息的索引
    child = GenericRelation(Child, related_query_name='yonghus')

    def __str__(self):
        return self.nickname


    # 用户身份认证模型
class Renzheng(models.Model):
    # 上传的验证图片
    ID_zheng = models.CharField(max_length=125, verbose_name='身份证正面图片', default='')
    ID_fan = models.CharField(max_length=125, verbose_name='身份证反面图片', default='')
    Ying = models.CharField(max_length=125, verbose_name='营业执照图片', default='')

    name = models.CharField(max_length=25, verbose_name='姓名', default='')
    nationality = models.CharField(max_length=8, verbose_name='民族', default='')
    id_num = models.CharField(max_length=18, verbose_name='身份证号', default='')
    sex = models.CharField(max_length=2, verbose_name='性别', default='')
    birth = models.CharField(max_length=10, verbose_name='出生日期', default='')
    address = models.CharField(max_length=256, verbose_name='家庭地址', default='')
    start_date = models.CharField(max_length=10, verbose_name='有效期起始时间', default='')
    end_date = models.CharField(max_length=10, verbose_name='有效期结束时间', default='')
    issue = models.CharField(max_length=32, verbose_name='签发机关', default='')

    zhuce_num = models.CharField(max_length=30, verbose_name='注册号', default='')
    fading_daibiao = models.CharField(max_length=25, verbose_name='法定代表人', default='')
    compuny = models.CharField(max_length=125, verbose_name='公司名称', default='')
    cp_address = models.CharField(max_length=125, verbose_name='公司地址', default='')
    cp_data = models.CharField(max_length=60, verbose_name='营业期限', default='')

    # 审核状态
    status = models.CharField(max_length=8, default='审核中', verbose_name='审核状态')
    # 关联用户这张表
    yonghu = models.OneToOneField('Yonghu', on_delete=models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return self.name
