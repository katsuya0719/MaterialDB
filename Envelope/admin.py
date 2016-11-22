from django.contrib import admin
from .models import Glass
#from import_export import resources
#from import_export.admin import ImportExportModelAdmin

# Register your models here.
admin.site.register(Glass)

"""
class GlassResource(resources.ModelResource):

	class Meta:
		model = Glass

class GlassAdmin(ImportExportModelAdmin):
	pass
"""
