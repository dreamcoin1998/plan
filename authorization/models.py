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

    def has_related_object(self):
        has_renzheng = False
        try:
            has_renzheng = (self.renzheng is not None)
        except Renzheng.DoesNotExist:
            pass
        return has_renzheng


    # 用户身份认证模型
class Renzheng(models.Model):
    # 上传的验证图片
    ID_zheng = models.CharField(max_length=125, verbose_name='身份证正面图片', default='')
    ID_fan = models.CharField(max_length=125, verbose_name='身份证反面图片', default='')
    Ying = models.CharField(max_length=125, verbose_name='营业执照图片', default='')

    name = models.CharField(max_length=25, verbose_name='姓名')
    nationality = models.CharField(max_length=8, verbose_name='民族')
    id_num = models.CharField(max_length=18, verbose_name='身份证号')
    sex = models.CharField(max_length=2, verbose_name='性别')
    birth = models.CharField(max_length=8, verbose_name='出生日期')
    address = models.CharField(max_length=256, verbose_name='家庭地址')
    start_date = models.CharField(max_length=8, verbose_name='有效期起始时间')
    end_date = models.CharField(max_length=8, verbose_name='有效期结束时间')
    issue = models.CharField(max_length=32, verbose_name='签发机关')

    # 审核状态
    status = models.CharField(max_length=8, default='审核中', verbose_name='审核状态')
    # 关联用户这张表
    yonghu = models.OneToOneField('Yonghu', on_delete=models.DO_NOTHING, blank=True, null=True)
