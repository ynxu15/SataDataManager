# -*- coding: utf-8 -*-
 
#from django.http import HttpResponse
from django.shortcuts import render
 
def proIntroView(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'test.html', context)