# -*- coding: utf-8 -*-
 
#from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
import json
 
def govPolicyView(request):
    context          = {}
    context['hello'] = 'Hello World!'
    #return render(request, 'tb.html', context)
    return render(request, 'govPolicyMacroRegion.html', context)


def govPolicyRegionView(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'govPolicyMacroRegion.html', context)

def comNum(request):
    print('aaaaa', request.POST.get('a'))
    a = list(range(10))
    return HttpResponse(json.dumps(a), content_type='application/json')

def govPolicyTimeView(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'govPolicyMacroTime.html', context)

def govPolicyBusinessView(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'govPolicyMacroBusiness.html', context)

def govPolicyComView(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'govPolicyMicroCom.html', context)

def govPolicyAnalysisView(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'govPolicyAnalysis.html', context)


def govPolicyAnalysisPredictionView(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'govPolicyAnalysisPrediction.html', context)


def govPolicyExampleView(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'govPolicyExamples.html', context)