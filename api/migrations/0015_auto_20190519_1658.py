# Generated by Django 2.0.6 on 2019-05-19 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_auto_20190519_1655'),
    ]

    operations = [
        migrations.AddField(
            model_name='child',
            name='school',
            field=models.CharField(default='暂无学校', max_length=50, verbose_name='学校'),
        ),
        migrations.AddField(
            model_name='child',
            name='school_area',
            field=models.CharField(default='暂无学校区域', max_length=50, verbose_name='学校区域'),
        ),
    ]
