# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, RequestFactory
from blog.models import Article
from django.utils import timezone
from django.contrib.auth.models import User


# Create your tests here.

class ArticleTestCase(TestCase):

	def setUp(self):
		self.factory = RequestFactory()
		self.user = User.objects.create_user(username='kenmartey', email='kenmartey@gmail.com', password='ceremony')

	def test_create_article(self):
		return Article.objects.create(
			title="this is a test title", 
			body="THis is a test body", 
			published_date=timezone.now(),
			author= self.user)
		
	# def test_create_article(self):
 #    	w = self.create_article()
 #    	self.assertTrue(isinstance(w, Arti))
 #    	self.assertEqual(w.__unicode__(), w.title)