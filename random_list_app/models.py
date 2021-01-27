# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class RandomList(models.Model):
    list_name = models.CharField(max_length=100)
    list_content = models.CharField(max_length=1000)
