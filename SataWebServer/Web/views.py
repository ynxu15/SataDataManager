# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request, 'index.html')

def back_page(request):
	return render(request, 'back.html')

def login(request):
	return render(request, 'login.html')