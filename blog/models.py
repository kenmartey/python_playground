# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from api_integration import settings
from django.utils import timezone

# Create your models here.

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')

class Article(models.Model):
	title = models.CharField(max_length=200, blank=True)
	body = models.TextField()
	published_date = models.DateTimeField(blank=True, null=True)
	author = models.ForeignKey(AUTH_USER_MODEL,  on_delete=models.CASCADE)



	def publish(self):
	    self.published_date = timezone.now()
	    self.save()

	def __unicode__(self):
	    return self.title

	def __str__(self):
	    return self.title

	class Meta:
	    verbose_name_plural = "Article"
