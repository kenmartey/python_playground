"""api_integration URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf import settings

from django.conf.urls import url, include
from django.contrib import admin
from blog.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index', index, name="index"),
    url(r'^$', landing_page, name="landing_page"),
    url(r'^article-detail/(?P<pk>\d+)$', article_detail, name='article_detail'),
    
    # api urls
    # url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^api/', include('restaurant_app.urls', namespace='api')),
    url(r'^twilio/', include('twilio_sms.urls')),
    url(r'^scrape/', include('scrape_app.urls')),

]
