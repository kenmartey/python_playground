# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from blog.models import *
from reporter.models import *

# Register your models here.
mybackendadmin = [Article, Reporters]
admin.site.register(mybackendadmin)