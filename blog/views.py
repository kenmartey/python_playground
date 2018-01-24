# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from blog.models import Article

# Create your views here.

def landing_page(request):
	return render(request, 'blog/landing_page.html')

def index(request):
	articles = Article.objects.all().order_by('-id')
	context = {
	'all_articles': articles
	}
	return render(request, 'blog/index.html', context)

def article_detail(request, pk):
	article_detail = get_object_or_404(Article, pk=pk)
	context = {
	'article': article_detail
	}
	return render(request, 'blog/article_detail.html', context)