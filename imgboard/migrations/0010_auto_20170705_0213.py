# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-04 23:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('imgboard', '0009_thread_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thread',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 4, 23, 13, 35, 918723, tzinfo=utc)),
        ),
    ]
