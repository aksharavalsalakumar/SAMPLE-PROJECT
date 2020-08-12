# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from newapp.models import User, ActivityPeriod

admin.site.register(User)
admin.site.register(ActivityPeriod)
