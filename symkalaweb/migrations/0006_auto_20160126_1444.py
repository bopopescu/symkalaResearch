# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-26 19:44


import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('symkalaweb', '0005_auto_20160126_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='key_expires',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 26, 19, 44, 30, 75000, tzinfo=utc)),
        ),
    ]
