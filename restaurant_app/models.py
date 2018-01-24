# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from api_integration import settings
from django.utils import timezone


AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')

class Restaurant(models.Model):
	name = models.CharField(max_length=200, blank=True)
	description = models.TextField()
	latitude = models.CharField(max_length=400, blank=True)
	longitude = models.CharField(max_length=400, blank=True)
	published_date = models.DateTimeField(blank=True, null=True)
	author = models.ForeignKey(AUTH_USER_MODEL,  on_delete=models.CASCADE)


	def publish(self):
	    self.published_date = timezone.now()
	    self.save()

	def __unicode__(self):
	    return self.name

	def __str__(self):
	    return self.name

	class Meta:
	    verbose_name_plural = "Restaurants"