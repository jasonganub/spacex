# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Launch


def display_all_launches(request):
    if request.method == 'GET':
        launches = Launch.objects.all()
        return render(request, 'launches.html', {'launches': launches})
