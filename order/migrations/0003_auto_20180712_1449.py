# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-12 14:49
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20180708_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.CharField(blank=True, default=uuid.UUID('a910a10b-314b-4558-91e3-9bfd3a39c102'), max_length=20, null=True),
        ),
    ]
