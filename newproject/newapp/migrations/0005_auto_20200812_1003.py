# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-08-12 10:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0004_auto_20200812_0305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activityperiod',
            name='end_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='activityperiod',
            name='start_time',
            field=models.DateTimeField(),
        ),
    ]