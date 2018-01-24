from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
admin.autodiscover()


from restaurant_app.api_views import *

router = DefaultRouter()
router.register(r'v1.0/restaurants', RestaurantViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]