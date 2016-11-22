from __future__ import unicode_literals

from django.db import models
from HVAC.models import BasicInfo

# Create your models here.
class Lighting(BasicInfo):
	lamp_type = models.CharField(max_length=50, blank = True)
	wattage = models.FloatField(null = True,blank=True)
	voltage = models.FloatField(null = True,blank=True)
	mercury = models.FloatField(null = True,blank=True)
	color_temp = models.IntegerField(null = True,blank=True)
	cri = models.IntegerField(null = True,blank=True)
	flux = models.FloatField(null = True,blank=True)
	efficacy = models.FloatField(null = True,blank=True)

	def __str__(self):
		return self.title


 