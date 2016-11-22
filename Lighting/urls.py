from django.conf.urls import url
from rest_framework import routers
from . import views

app_name = 'lighting'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
]
router = routers.DefaultRouter(trailing_slash=False)
router.register(r'lighting/', views.LightingViewSet)