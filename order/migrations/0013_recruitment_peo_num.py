# Generated by Django 2.0.6 on 2019-04-27 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0012_recruitment_pay_method'),
    ]

    operations = [
        migrations.AddField(
            model_name='recruitment',
            name='peo_num',
            field=models.PositiveIntegerField(default=100, verbose_name='人数'),
        ),
    ]