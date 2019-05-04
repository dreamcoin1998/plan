# Generated by Django 2.0.6 on 2019-04-27 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0011_auto_20190424_0126'),
    ]

    operations = [
        migrations.AddField(
            model_name='recruitment',
            name='pay_method',
            field=models.CharField(choices=[('Day', '日结'), ('Week', '周结'), ('Month', '月结'), ('Term', '学期')], default='Month', max_length=5, verbose_name='结算方式'),
        ),
    ]