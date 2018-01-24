import re
from rest_framework import permissions, status, generics, authentication
from rest_framework.decorators import detail_route, \
                    list_route, permission_classes, api_view
from rest_framework import viewsets
from rest_framework.status import (HTTP_201_CREATED,
                                   HTTP_200_OK,
                                   HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED,
                                   HTTP_404_NOT_FOUND)
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from restaurant_app.models import *
from restaurant_app.serializers import *


class RestaurantViewSet(viewsets.ModelViewSet):
	model = Restaurant
	serializer_class = RestaurantSerializer
	queryset = Restaurant.objects.all()


	@list_route(methods=('GET',), url_path='around-me')
	def restaurants_around_me(self, request, *args, **kwargs):
		around_me = Restaurant.objects.filter(latitude='5.6481059', longitude='-0.1446835')
		around_me = self.serializer_class(around_me, many=True)
		return Response({"status_code": HTTP_200_OK,
						"result": around_me.data

					})