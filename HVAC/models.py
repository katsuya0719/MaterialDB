from __future__ import unicode_literals

from django.db import models

# Create your models here.
class BasicInfo(models.Model):
	title = models.CharField(max_length=50)
	manufacturer = models.CharField(max_length=50, blank = True)
	used_project = models.CharField(max_length=50, blank = True)


class Chiller(BasicInfo):
	Capacity = models.IntegerField()


