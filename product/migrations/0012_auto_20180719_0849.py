# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-19 08:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_auto_20180719_0848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='arab',
            field=models.CharField(default='غير معروف', max_length=180),
        ),
        migrations.AlterField(
            model_name='productbrand',
            name='arab',
            field=models.CharField(default='غير معروف', max_length=180),
        ),
        migrations.AlterField(
            model_name='productoccasion',
            name='arab',
            field=models.CharField(default='غير معروف', max_length=180),
        ),
        migrations.AlterField(
            model_name='productrooms',
            name='arab',
            field=models.CharField(default='غير معروف', max_length=180),
        ),
        migrations.AlterField(
            model_name='productstyles',
            name='arab',
            field=models.CharField(default='غير معروف', max_length=180),
        ),
    ]
