# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-07 05:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_auto_20180706_1607'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='area',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='city',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='direction',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='house',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='jada',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='street',
        ),
    ]