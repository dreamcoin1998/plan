# Generated by Django 2.0.6 on 2019-05-19 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20190519_1258'),
    ]

    operations = [
        migrations.AddField(
            model_name='child',
            name='image',
            field=models.CharField(default='xxxxxxx', max_length=125, verbose_name='图片文件名称'),
        ),
    ]
