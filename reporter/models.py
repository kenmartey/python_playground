# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from api_integration import settings
from django.utils import timezone
from blog.models import Article
# Create your models here.

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')

class Reporters(models.Model):
	reporter_name = models.CharField(max_length=200, blank=True)
	article_reported = models.ForeignKey(Article, on_delete=models.CASCADE)
	published_date = models.DateTimeField(blank=True, null=True)
	author = models.OneToOneField(AUTH_USER_MODEL,  on_delete=models.CASCADE, null=True)



	def publish(self):
	    self.published_date = timezone.now()
	    self.save()

	def __unicode__(self):
	    return self.reporter_name

	def __str__(self):
	    return self.reporter_name

	class Meta:
	    verbose_name_plural = "reporter_name"