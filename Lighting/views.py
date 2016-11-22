from django.shortcuts import render
from django.views import generic
from .models import Lighting
from rest_framework import viewsets, filters
from .serializer import LightingSerializer

# Create your views here.
class IndexView(generic.ListView):
	template_name = 'lighting/index.html'
	context_object_name = 'lighting_list'
	def get_queryset(self):
		return Lighting.objects.order_by('-wattage')[:5]

class LightingViewSet(viewsets.ModelViewSet):
	queryset = Lighting.objects.all()
	serializer_class = LightingSerializer

