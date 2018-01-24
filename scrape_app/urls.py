from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin


from scrape_app.views import *


urlpatterns = [
    url(r'scrape-site', fetch_page_content, name='send_sms'),

]