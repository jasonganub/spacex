# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Launch(models.Model):
    date = models.DateField("date launched")
    customer = models.CharField(max_length=100)
    launch_site = models.CharField(max_length=100)
    vehicle = models.CharField(max_length=100)

    def __str__(self):
        return "{}: {}".format(str(self.date), self.vehicle)
