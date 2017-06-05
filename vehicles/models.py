# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Vehicle(models.Model):
    name = models.CharField(max_length=100)
    height = models.FloatField(default=0)
    diameter = models.FloatField(default=0)
    mass = models.IntegerField(default=0)
    stages = models.IntegerField(default=0)
    payload_to_leo = models.IntegerField(default=0)
    payload_to_gto = models.IntegerField(default=0)
    payload_to_mars = models.IntegerField(default=0)

    def __str__(self):
        return self.name
