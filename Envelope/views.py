from django.shortcuts import render
from django.views import generic
from .models import Glass
from .forms import UploadFileForm
from rest_framework import viewsets, filters
from .serializer import GlassSerializer

# Create your views here.
class GlassIndex(generic.ListView):
	template_name = 'envelope/index.html'
	context_object_name = 'glass_list'
	def get_queryset(self):
		return Glass.objects.order_by('-title')[:5]

class DataView(generic.FormView):
	template_name = 'envelope/upload.html'
	form_class=UploadFileForm
	success_url='/upload/'

	def form_valid(self, form):
		form.process_data()
		return super().form_valid(form)

class GlassViewSet(viewsets.ModelViewSet):
	queryset = Glass.objects.all()
	serializer_class = GlassSerializer
