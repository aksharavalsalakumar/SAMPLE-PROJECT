# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class User(models.Model):
    id = models.CharField(primary_key=True, unique=True, max_length=500)
    real_name = models.CharField(max_length=500)
    tz = models.CharField(max_length=500)


class ActivityPeriod(models.Model):
    fk = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
