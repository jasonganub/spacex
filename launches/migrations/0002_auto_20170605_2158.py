# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-06 04:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('launches', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='launch',
            name='location',
        ),
        migrations.RemoveField(
            model_name='launch',
            name='name',
        ),
        migrations.AddField(
            model_name='launch',
            name='customer',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='launch',
            name='launch_site',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]