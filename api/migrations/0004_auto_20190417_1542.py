# Generated by Django 2.0.6 on 2019-04-17 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20190417_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shangjia',
            name='location',
            field=models.CharField(max_length=255, null=True, verbose_name='商家地址'),
        ),
    ]
