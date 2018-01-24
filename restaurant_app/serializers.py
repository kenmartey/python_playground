from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.http import Http404, HttpResponseForbidden
from rest_framework.decorators import (api_view, permission_classes, list_route)
from django.core.validators import validate_email
from rest_framework.serializers import ModelSerializer
from restaurant_app.models import *


class RestaurantSerializer(serializers.ModelSerializer):

	class Meta:
		model = Restaurant
		fields = ('id', 'name','description', 'longitude', 'latitude')