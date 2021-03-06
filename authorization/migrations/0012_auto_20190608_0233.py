# Generated by Django 2.0.6 on 2019-06-07 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0011_auto_20190607_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='renzheng',
            name='address',
            field=models.CharField(default='', max_length=256, verbose_name='家庭地址'),
        ),
        migrations.AlterField(
            model_name='renzheng',
            name='birth',
            field=models.CharField(default='', max_length=8, verbose_name='出生日期'),
        ),
        migrations.AlterField(
            model_name='renzheng',
            name='end_date',
            field=models.CharField(default='', max_length=8, verbose_name='有效期结束时间'),
        ),
        migrations.AlterField(
            model_name='renzheng',
            name='id_num',
            field=models.CharField(default='', max_length=18, verbose_name='身份证号'),
        ),
        migrations.AlterField(
            model_name='renzheng',
            name='issue',
            field=models.CharField(default='', max_length=32, verbose_name='签发机关'),
        ),
        migrations.AlterField(
            model_name='renzheng',
            name='name',
            field=models.CharField(default='', max_length=25, verbose_name='姓名'),
        ),
        migrations.AlterField(
            model_name='renzheng',
            name='nationality',
            field=models.CharField(default='', max_length=8, verbose_name='民族'),
        ),
        migrations.AlterField(
            model_name='renzheng',
            name='sex',
            field=models.CharField(default='', max_length=2, verbose_name='性别'),
        ),
        migrations.AlterField(
            model_name='renzheng',
            name='start_date',
            field=models.CharField(default='', max_length=8, verbose_name='有效期起始时间'),
        ),
    ]
