from django.conf.urls import url
from rest_framework import routers
from . import views

app_name = 'envelope'
urlpatterns = [
    url(r'^$', views.GlassIndex.as_view(), name='index'),
    url(r'^upload/',views.DataView.as_view(),name='csv_upload')
    #url(r'^upload/', csvUpload.as_view(), name='csv_upload'),
]
router = routers.DefaultRouter(trailing_slash=False)
router.register(r'api/', views.GlassViewSet)

urlpatterns += router.urls