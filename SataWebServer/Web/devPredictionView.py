# coding=utf-8
#from django.http import HttpResponse
from django.shortcuts import render

def predictMainView(request):
    context          = {}
    # context['hello'] = 'Hello World!'
    return render(request, 'predictMain.html', context)

def predictPartView(request):
    context          = {}
    context['title'] = '某区某行业'
    return render(request, 'predictPart.html', context)

def predictComView(request):
    context          = {}
    context['title'] = '公司'
    return render(request, 'predictCom.html', context)