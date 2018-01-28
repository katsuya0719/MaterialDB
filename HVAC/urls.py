from django.conf.urls import url
from rest_framework import routers
from .views import ChillerList,ChillerDetail,idf_import

app_name = "hvac"
urlpatterns = [
    url(r'^$',ChillerList.as_view(), name='chiller'),
    url(r'^(?P<pk>\d+)/$',ChillerDetail.as_view(), name='detail'),
    url(r'^import/$', idf_import, name='import'),
]