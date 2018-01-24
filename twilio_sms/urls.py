from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin


from twilio_sms.views import *


urlpatterns = [
    url(r'send-sms', send_sms, name='send_sms'),

]