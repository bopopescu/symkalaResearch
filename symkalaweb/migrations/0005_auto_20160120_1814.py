# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-20 23:14
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('symkalaweb', '0004_auto_20160118_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='key_expires',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 20, 23, 14, 19, 661000, tzinfo=utc)),
        ),
    ]
