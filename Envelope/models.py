from __future__ import unicode_literals

from django.db import models
from HVAC.models import BasicInfo

# Create your models here.
class Glass(BasicInfo):
	thickness = models.FloatField(null = True,blank=True)
	tsol = models.FloatField(null = True,blank=True)
	rsol1 = models.FloatField(null = True,blank=True)
	rsol2 = models.FloatField(null = True,blank=True)
	tvis = models.FloatField(null = True,blank=True)
	rvis1 = models.FloatField(null = True,blank=True)
	rvis2 = models.FloatField(null = True,blank=True)
	emis1 = models.FloatField(null = True,blank=True)
	emis2 = models.FloatField(null = True,blank=True)
	conductivity = models.FloatField(null = True,blank=True)
	tvis2 = models.FloatField(null = True,blank=True)
	tsol2 = models.FloatField(null = True,blank=True)

	def __str__(self):
		return self.title