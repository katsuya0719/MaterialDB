# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-14 08:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HVAC', '0003_basicinfo_used_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicinfo',
            name='manufacturer',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
