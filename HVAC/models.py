from __future__ import unicode_literals

from django.db import models

# Create your models here.
class BasicInfo(models.Model):
	title = models.CharField(max_length=100)
	manufacturer = models.CharField(max_length=50, blank = True)
	used_project = models.CharField(max_length=50, null=True,blank=True)
	cost=models.IntegerField(null = True, blank = True)
	url=models.URLField(null=True,blank=True)
	comment=models.TextField(null=True,blank=True)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title

class VRV(BasicInfo):
	InletT = models.FloatField(blank=True)
	OutletT = models.FloatField(blank=True)
	Capacity = models.IntegerField(blank=True)  # Reference capacity
	COP = models.FloatField(blank=True)  # Reference COP

class CapacityFunction(models.Model):
	name=models.CharField(max_length=100, blank = True)
	c1=models.FloatField()
	c2=models.FloatField()
	c3 = models.FloatField()
	c4 = models.FloatField()
	c5 = models.FloatField()
	c6 = models.FloatField()
	minX= models.FloatField(blank=True)
	maxX = models.FloatField(blank=True)
	minY = models.FloatField(blank=True)
	maxY = models.FloatField(blank=True)

	def __str__(self):
		return self.name

class EIRofTemp(CapacityFunction):
	pass

class EIRofPLR(models.Model):
	name = models.CharField(max_length=100, blank=True)
	c1=models.FloatField()
	c2= models.FloatField()
	c3 = models.FloatField()
	c4 = models.FloatField(blank=True,null=True)
	minX = models.FloatField(blank=True)
	maxX = models.FloatField(blank=True)

	def __str__(self):
		return self.name

class Chiller(BasicInfo):
	capacity = models.IntegerField(blank=True)  # Reference capacity
	cop = models.FloatField(blank=True)  # Reference COP
	chwtemp=models.FloatField(blank=True)
	cwtemp = models.FloatField(blank=True)
	CONDENSER_CHOICES = (
		('WaterCooled','WaterCooled'),
		('AirCooled', 'AirCooled'),
		('EvaporativelyCooled','EvaporativelyCooled')
	)
	Condenser=models.CharField(max_length=15,choices=CONDENSER_CHOICES,default='Water')
	CHWFlowRate=models.FloatField(blank=True,null=True)
	CWFlowRate=models.FloatField(blank=True,null=True)
	minPLR=models.FloatField(blank=True,null=True)
	maxPLR=models.FloatField(blank=True,null=True)
	optimumPLR=models.FloatField(blank=True,null=True)
	minUnloadRatio=models.FloatField(blank=True,null=True)
	CapacityFunction=models.OneToOneField(CapacityFunction,blank=True,null=True,on_delete=models.CASCADE,related_name='cap')
	EIRofTemp=models.OneToOneField(EIRofTemp,blank=True,null=True,on_delete=models.CASCADE,related_name='eirtemp')
	EIRofPLR = models.OneToOneField(EIRofPLR, blank=True,null=True, on_delete=models.CASCADE,related_name='eirplr')

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

#class WaterPump(BasicInfo):






