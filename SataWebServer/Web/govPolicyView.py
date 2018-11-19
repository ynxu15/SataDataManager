# -*- coding: utf-8 -*-
 
#from django.http import HttpResponse
from django.shortcuts import render
 
def govPolicyView(request):
    context          = {}
    context['hello'] = 'Hello World!'
    #return render(request, 'tb.html', context)
    return render(request, 'base_govPolicy1.html', context)