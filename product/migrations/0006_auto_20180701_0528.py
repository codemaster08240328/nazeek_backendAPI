# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-01 05:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20180701_0459'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='overview',
            new_name='review',
        ),
    ]
