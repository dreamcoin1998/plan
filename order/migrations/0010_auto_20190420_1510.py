# Generated by Django 2.0.6 on 2019-04-20 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0009_auto_20190420_1416'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_pingjia',
            field=models.BooleanField(default=False, verbose_name='是否已经评价'),
        ),
        migrations.AlterField(
            model_name='recruitment',
            name='is_stop',
            field=models.BooleanField(default=False, verbose_name='是否结束'),
        ),
    ]
