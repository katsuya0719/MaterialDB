from django.conf.urls import url
from rest_framework import routers
from .views import ChillerList,ChillerDetail,idf_import,Graph,ChartData

app_name = "hvac"
urlpatterns = [
    url(r'^$',ChillerList.as_view(), name='list'),
    url(r'^search/$',Graph, name='search'),
    url(r'^api/chart/data/$', ChartData.as_view(), name='api-chart-data'),
    url(r'^api/(?P<pk>\d+)/$',ChillerDetail.as_view(), name='api-detail'),
    url(r'^(?P<pk>\d+)/$',ChillerDetail.as_view(), name='detail'),
    url(r'^import/$', idf_import, name='import'),
]