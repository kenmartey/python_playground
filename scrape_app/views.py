# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
# import libraries
import urllib2
from bs4 import BeautifulSoup

# save data to csv
import csv
from datetime import datetime
# Create your views here.


# declare the url 
def fetch_page_content(request):
	get_items = []
	quote_page = 'http://www.bloomberg.com/quote/SPX:IND'
	# query the website and return the html to the variable ‘page’
	page = urllib2.urlopen(quote_page)
	# pull out data of the html 
	soup = BeautifulSoup(page, 'html.parser')
	# We get the tag with .find() method in soup
	name_box = soup.find('h1', attrs={'class': 'name'})
	# after the tag we get the inner element by stripping the tag
	name = name_box.text.strip()
	price_tag = soup.find('div', attrs={'class': 'price'})
	price = price_tag.text
	get_items.append(name)
	get_items.append(price)
	print get_items

	with open('scraped_data', 'a') as csv_file:
		writer = csv.writer(csv_file)
		writer.writerow([name,price,datetime.now()])

	context = {
	'soup': name
	}
	return render(request, 'scrape_site/scrape.html', context)
