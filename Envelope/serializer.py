from rest_framework import serializers
from .models import Glass

class GlassSerializer(serializers.ModelSerializer):

	class Meta:
		model = Glass
		fields = ('title','manufacturer','thickness','tsol','rsol1','rsol2','tvis','rvis1','rvis2','emis1','emis2','conductivity','tvis2','tsol2')