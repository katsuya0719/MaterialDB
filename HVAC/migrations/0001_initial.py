# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-20 12:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BasicInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('manufacturer', models.CharField(max_length=50)),
                ('used_project', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Chiller',
            fields=[
                ('basicinfo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='HVAC.BasicInfo')),
                ('Capacity', models.IntegerField()),
            ],
            bases=('HVAC.basicinfo',),
        ),
    ]
