from __future__ import unicode_literals

from django.db import models

# Create your models here.
class BasicInfo(models.Model):
	title = models.CharField(max_length=50)
	manufacturer = models.CharField(max_length=50, blank = True)
	used_project = models.CharField(max_length=50, blank = True)
	cost=models.IntegerField(null = True)
	url=models.URLField(null=True,blank=True)
	comment=models.TextField(blank=True)
	created_at = models.DateTimeField(auto_now_add=True)

class VRV(BasicInfo):
	InletT = models.FloatField(blank=True)
	OutletT = models.FloatField(blank=True)
	Capacity = models.IntegerField(blank=True)  # Reference capacity
	COP = models.FloatField(blank=True)  # Reference COP

class Chiller(VRV):
	CONDENSER_CHOICES = (
		('WaterCooled','WaterCooled'),
		('AirCooled', 'AirCooled'),
		('EvaporativelyCooled','EvaporativelyCooled')
	)
	Condenser=models.CharField(max_length=15,choices=CONDENSER_CHOICES,default='Water')

class HeatExchanger(BasicInfo):
	Efficiency=models.IntegerField(blank=True)
	AirVolume=models.IntegerField(blank=True)
	Noise=models.IntegerField(blank=True)
	Consumption=models.IntegerField(blank=True)

class FCU(BasicInfo):
	AirVolume=models.IntegerField(blank=True)
	SensibleCoolCap=models.IntegerField(blank=True)
	LatentCoolCap = models.IntegerField(blank=True)
	HeatCap=models.IntegerField(blank=True)
	WaterFlow=models.IntegerField(blank=True)
	Noise=models.IntegerField(blank=True)

class WaterPump(BasicInfo):






