# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-23 00:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('HVAC', '0005_auto_20161122_2227'),
    ]

    operations = [
        migrations.AddField(
            model_name='basicinfo',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]