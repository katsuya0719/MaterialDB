from django.contrib import admin
from .models import Glass,Insulation
#from import_export import resources
#from import_export.admin import ImportExportModelAdmin

# Register your models here.
admin.site.register(Glass)
admin.site.register(Insulation)

"""
class GlassResource(resources.ModelResource):

	class Meta:
		model = Glass

class GlassAdmin(ImportExportModelAdmin):
	pass
"""
