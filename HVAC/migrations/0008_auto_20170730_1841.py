# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2017-07-30 09:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HVAC', '0007_auto_20170730_1806'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeatExchanger',
            fields=[
                ('basicinfo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='HVAC.BasicInfo')),
                ('Efficiency', models.IntegerField(blank=True)),
                ('AirVolume', models.IntegerField(blank=True)),
                ('Noise', models.IntegerField(blank=True)),
                ('Consumption', models.IntegerField(blank=True)),
            ],
            bases=('HVAC.basicinfo',),
        ),
        migrations.CreateModel(
            name='VRV',
            fields=[
                ('basicinfo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='HVAC.BasicInfo')),
                ('InletT', models.FloatField(blank=True)),
                ('OutletT', models.FloatField(blank=True)),
                ('Capacity', models.IntegerField(blank=True)),
                ('COP', models.FloatField(blank=True)),
            ],
            bases=('HVAC.basicinfo',),
        ),
        migrations.RemoveField(
            model_name='chiller',
            name='COP',
        ),
        migrations.RemoveField(
            model_name='chiller',
            name='Capacity',
        ),
        migrations.RemoveField(
            model_name='chiller',
            name='InletT',
        ),
        migrations.RemoveField(
            model_name='chiller',
            name='OutletT',
        ),
        migrations.RemoveField(
            model_name='chiller',
            name='basicinfo_ptr',
        ),
        migrations.AddField(
            model_name='chiller',
            name='vrv_ptr',
            field=models.OneToOneField(auto_created=True, default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='HVAC.VRV'),
            preserve_default=False,
        ),
    ]
