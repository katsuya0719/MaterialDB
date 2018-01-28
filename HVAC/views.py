from django.shortcuts import render
from django.views.generic import ListView
from .models import Chiller
# Create your views here.

class IndexView(ListView):
    template_name = 'lighting/index.html'
    model = Chiller