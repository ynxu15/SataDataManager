# -*- coding: utf-8 -*-
 
#from django.http import HttpResponse
from django.shortcuts import render
 
def indexView(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'index.html', context)