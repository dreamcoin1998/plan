# Generated by Django 2.0.6 on 2019-04-17 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_delete_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='shangjia',
            name='latitude',
            field=models.PositiveIntegerField(null=True, verbose_name='用户所在纬度'),
        ),
        migrations.AddField(
            model_name='shangjia',
            name='longitude',
            field=models.PositiveIntegerField(null=True, verbose_name='用户所在经度'),
        ),
    ]