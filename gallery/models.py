# coding: utf-8
# Copyright (c) 2011 Aymeric Augustin. All rights reserved.

from django.conf import settings
from django.db import models


class Album(models.Model):
    dirpath = models.CharField(max_length=200, unique=True)
    date = models.DateField(null=True, blank=True)
    name = models.CharField(max_length=100, blank=True)


class Photo(models.Model):
    album = models.ForeignKey(Album)
    filename = models.CharField(max_length=100)
    date = models.DateTimeField(null=True, blank=True)
