# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title



class data(models.Model):
    name = models.CharField(max_length=10)
    ids = models.CharField(max_length=5)
    result = models.CharField(max_length=2)

    def __str__(self):
        return self.name
