# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-19 08:49
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0012_auto_20180719_0848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.CharField(blank=True, default=uuid.UUID('915966cd-578d-419a-bb4f-582fc5016cda'), max_length=20, null=True),
        ),
    ]
