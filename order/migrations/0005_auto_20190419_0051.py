# Generated by Django 2.0.6 on 2019-04-18 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_auto_20190417_0148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recruitment',
            name='user',
            field=models.ManyToManyField(blank=True, null=True, related_name='user', to='authorization.Yonghu'),
        ),
    ]
