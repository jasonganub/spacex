# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Launch(models.Model):
    name = models.CharField(max_length=100)
    vehicle = models.CharField(max_length=100)
    date = models.DateTimeField("date launched")
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name
