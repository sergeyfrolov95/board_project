# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-04 22:58
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imgboard', '0008_auto_20170612_1234'),
    ]

    operations = [
        migrations.AddField(
            model_name='thread',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
