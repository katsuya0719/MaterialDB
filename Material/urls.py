"""Material URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include,url
from django.contrib import admin
#from Lighting.urls import router
from Envelope.urls import router
from django.views.generic import RedirectView

urlpatterns = [
	url(r'^lighting/', include('Lighting.urls')),
	url(r'^envelope/', include('Envelope.urls')),
	url(r'^hvac/', include('HVAC.urls')),
    url(r'^admin/', admin.site.urls),
    #url(r'^api/', include(router.urls)),
    #url('', RedirectView.as_view(url='/static/index.html')),
]
