# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Article(models.Model):
    bf_15 = models.IntegerField(u'收入（2015年）')
    bf_16 = models.IntegerField(u'收入（2016年）')
    bf_17 = models.IntegerField(u'收入（2017年）')
    pub_date = models.DateTimeField(u'添加时间', auto_now_add=True, editable = True)