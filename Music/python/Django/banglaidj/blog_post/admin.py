# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import post
from .models import data

# Register your models here.


admin.site.register(post)
admin.site.register(data)