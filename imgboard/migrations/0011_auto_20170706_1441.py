# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-06 11:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('imgboard', '0010_auto_20170705_0213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thread',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
