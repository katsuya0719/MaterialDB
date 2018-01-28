from django.contrib import admin
from .models import Chiller,CapacityFunction,EIRofTemp,EIRofPLR

# Register your models here.
admin.site.register(Chiller)
admin.site.register(CapacityFunction)
admin.site.register(EIRofTemp)
admin.site.register(EIRofPLR)