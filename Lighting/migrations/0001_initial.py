# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-20 12:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('HVAC', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lighting',
            fields=[
                ('basicinfo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='HVAC.BasicInfo')),
                ('lamp_type', models.CharField(max_length=50)),
                ('wattage', models.IntegerField()),
                ('voltage', models.IntegerField()),
                ('mercury', models.IntegerField()),
                ('color_temp', models.IntegerField()),
                ('flux', models.IntegerField()),
                ('efficacy', models.IntegerField()),
            ],
            bases=('HVAC.basicinfo',),
        ),
    ]
