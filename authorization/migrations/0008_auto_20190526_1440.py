# Generated by Django 2.0.6 on 2019-05-26 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0007_renzheng'),
    ]

    operations = [
        migrations.AddField(
            model_name='renzheng',
            name='ID_fan',
            field=models.CharField(default='', max_length=125, verbose_name='身份证反面图片'),
        ),
        migrations.AddField(
            model_name='renzheng',
            name='ID_zheng',
            field=models.CharField(default='', max_length=125, verbose_name='身份证正面图片'),
        ),
        migrations.AddField(
            model_name='renzheng',
            name='Ying',
            field=models.CharField(default='', max_length=125, verbose_name='营业执照图片'),
        ),
    ]