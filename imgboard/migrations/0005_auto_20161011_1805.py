# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-11 15:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imgboard', '0004_auto_20161011_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pic',
            field=models.ImageField(blank=True, upload_to='pictures'),
        ),
    ]
