"商家评价 模型类"


from django.db import models
from authorization.models import Yonghu
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from api.models import Shangjia
from order.models import Order

# 商家评价
class Evaluation(models.Model):
    # 商家评分——可选星星数量
    STAR_NUMBER = (
        (1, '一颗星'),
        (2, '两颗星'),
        (3, '三颗星'),
        (4, '四颗星'),
        (5, '五颗星')
    )
    # 商家星级
    star = models.PositiveIntegerField(choices=STAR_NUMBER, default=5, verbose_name='商家星级')
    # 商家评分
    score = models.PositiveIntegerField(default=5, verbose_name='商家评分')
    # 商家评价
    evaluation_text = models.TextField(verbose_name='评价内容')
    # 提交时间
    comment_time = models.DateTimeField(auto_now_add=True)

    # 外键，主要用来联结 评价的用户和商家
    yonghu = models.ForeignKey(Yonghu, on_delete=models.DO_NOTHING, verbose_name='评价的用户', null=True)
    order = models.ForeignKey(Order, on_delete=models.DO_NOTHING, verbose_name='属于的订单', null=True)
    class Meta:
        ordering = ['-comment_time'] # 按发布时间排序