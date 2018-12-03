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

def dataImport(request):
    context          = {}
    context['title'] = '数据导入'
    return render(request, 'dataImport.html', context)

def dataExport(request):
    context          = {}
    context['title'] = '数据导出'
    return render(request, 'dataExport.html', context)

def dataUpdate(request):
    context          = {}
    context['title'] = '数据修改'
    return render(request, 'dataUpdate.html', context)

def dataClean(request):
    context          = {}
    context['title'] = '数据导出'
    return render(request, 'dataClean.html', context)