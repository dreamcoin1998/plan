# Generated by Django 2.0.6 on 2019-04-16 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recruitment',
            name='work_location',
            field=models.CharField(max_length=256, verbose_name='工作地点'),
        ),
    ]
