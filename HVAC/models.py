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

class Chiller(BasicInfo):
	capacity = models.IntegerField(blank=True)  # Reference capacity
	cop = models.FloatField(blank=True)  # Reference COP
	chwtemp=models.FloatField(blank=True)
	conwtemp = models.FloatField(blank=True)
	chwfr=models.FloatField(blank=True,null=True)
	conwfr=models.FloatField(blank=True,null=True)
	#capfunc=models.OneToOneField(CapacityFunction,blank=True,null=True,on_delete=models.CASCADE,related_name='cap')
	#eiroftemp=models.OneToOneField(EIRofTemp,blank=True,null=True,on_delete=models.CASCADE,related_name='eirtemp')
	#eirofplr = models.OneToOneField(EIRofPLR, blank=True,null=True, on_delete=models.CASCADE,related_name='eirplr')
	minplr=models.FloatField(blank=True,null=True)
	maxplr=models.FloatField(blank=True,null=True)
	optimumplr=models.FloatField(blank=True,null=True)
	minunloadratio=models.FloatField(blank=True,null=True)
	CONDENSER_CHOICES = (
		('WaterCooled','WaterCooled'),
		('AirCooled', 'AirCooled'),
		('EvaporativelyCooled','EvaporativelyCooled')
	)
	condenser=models.CharField(max_length=15,choices=CONDENSER_CHOICES,default='WaterCooled')
	FLOWMODE_CHOICES = (
		('ConstantFlow','ConstantFlow'),
		('NotModulated', 'NotModulated'),
		('LeavingSetpointModulated','LeavingSetpointModulated')
	)
	flowmode=models.CharField(max_length=50,choices=FLOWMODE_CHOICES,default='ConstantFlow')

class CapacityFunction(models.Model):
	chiller=models.ForeignKey(Chiller,related_name='cap')
	name=models.CharField(max_length=100, blank = True)
	c1=models.FloatField()
	c2=models.FloatField()
	c3 = models.FloatField()
	c4 = models.FloatField()
	c5 = models.FloatField()
	c6 = models.FloatField()
	min_x= models.FloatField(blank=True)
	max_x = models.FloatField(blank=True)
	min_y = models.FloatField(blank=True)
	max_y = models.FloatField(blank=True)

	def __str__(self):
		return self.name

class EIRofTemp(models.Model):
	base_chiller = models.ForeignKey(Chiller, related_name='eirtemp')
	name = models.CharField(max_length=100, blank=True)
	c1 = models.FloatField()
	c2 = models.FloatField()
	c3 = models.FloatField()
	c4 = models.FloatField()
	c5 = models.FloatField()
	c6 = models.FloatField()
	min_x = models.FloatField(blank=True)
	max_x = models.FloatField(blank=True)
	min_y = models.FloatField(blank=True)
	max_y = models.FloatField(blank=True)

	def __str__(self):
		return self.name

class EIRofPLR(models.Model):
	chiller = models.ForeignKey(Chiller,related_name='eirplr')
	name = models.CharField(max_length=100, blank=True)
	c1=models.FloatField()
	c2= models.FloatField()
	c3 = models.FloatField()
	c4 = models.FloatField(blank=True,null=True)
	min_x = models.FloatField(blank=True)
	max_x = models.FloatField(blank=True)

	def __str__(self):
		return self.name

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






