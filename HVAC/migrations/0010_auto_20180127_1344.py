# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-27 04:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HVAC', '0009_auto_20180127_1334'),
    ]

    operations = [
        migrations.AddField(
            model_name='capacityfunction',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='eirofplr',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
