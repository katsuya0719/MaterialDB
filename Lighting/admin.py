from django.contrib import admin
from .models import Lighting
#from import_export import resources

# Register your models here.
admin.site.register(Lighting)

#class LightingResource(resources.ModelResource):

#	class Meta:
#		model = Lighting
