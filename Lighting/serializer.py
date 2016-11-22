from rest_framework import serializers
from .models import Lighting

class LightingSerializer(serializers.ModelSerializer):

	class Meta:
		model = Lighting
		fields = ('title','lamp_type','wattage','voltage','mercury','color_temp','cri','flux','efficacy','manufacturer')