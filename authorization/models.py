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