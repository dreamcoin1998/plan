from django.db import models

# 用户模型
class Yonghu(models.Model):
    # open_id
    open_id = models.CharField(max_length=64, unique=True)
    # 昵称
    nickname = models.CharField(max_length=256)

    def __str__(self):
        return self.nickname