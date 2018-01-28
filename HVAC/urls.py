from django.conf.urls import url
from rest_framework import routers
from .views import IndexView

app_name = 'hvac'
urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
]