# Generated by Django 2.0.6 on 2019-05-19 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_child_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='image',
            field=models.CharField(max_length=125, verbose_name='图片文件名称'),
        ),
    ]
