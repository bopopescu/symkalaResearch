# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-09 17:46
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('symkalaweb', '0011_auto_20160429_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='key_expires',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 9, 17, 45, 55, 723000, tzinfo=utc)),
        ),
    ]