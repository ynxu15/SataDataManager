# coding=utf-8
#from django.http import HttpResponse
from django.shortcuts import render
from django import forms
from django.template import RequestContext
from models import Eps
from django.db.models import Count
import json
from django.http import HttpResponse
from django.template import RequestContext, loader

regionCode = {'浦东':'01', '黄浦':'02', '静安':'03', '徐汇':'04', '长宁':'05', '普陀':'06', '虹口':'07', '杨浦':'08', '宝山':'09', '闵行':'10',
            '嘉定':'11', '金山':'12', '松江':'13','青浦':'14','奉贤':'15','崇明':'16'}
industryTypes = ['A', 'B', 'C', 'D', 'E']
def predictMainView(request):
    context          = {}
    context['title'] = '上海市'

    li = list(Eps.objects.all().values('com_region','com_type').annotate(count=Count('id')).values('count','com_region','com_type'))

    counts = []
    for p in li:
        counts.append(p['count'])

    context['li'] = counts

    return render(request, 'predictMain.html', context)

def predictPartView(request):
    context          = {}
    context['title'] = '某区某行业'

    regioncount = Eps.objects.all().values('com_region').annotate(count=Count('id')).values('count','com_region')

    value = []
    name = []
    for p in regioncount:
        value.append(p['count'])
        name.append(p['com_region'])
    d = []
    for i in range(len(value)):
        d.append({'value':value[i],'name':name[i]})
    context['region'] = json.dumps(d)

    typecount = Eps.objects.all().values('com_type').annotate(count=Count('id')).values('count','com_type')

    value = []
    name = []
    for p in typecount:
        value.append(p['count'])
        name.append(p['com_type'])
    d = []
    for i in range(len(value)):
        d.append({'value':value[i],'name':name[i]})
    context['type'] = json.dumps(d)
    

    return render(request, 'predictPart.html', context)

def getEpsByRegionAndType(request):
    name_dict = {'twz': 'Love python and Django', 'zqxt': 'I am teaching Django'}
    return HttpResponse(json.dumps(name_dict), content_type='application/json')

def predictComView(request):
    # id = 0
    # if request.method == 'GET':
    #     id = request.GET.get('id')
    # print id
    # com_list = Eps.objects.raw('select * from Web_Eps where id = '+str(id))
    # for p in com_list:
    #     print p.id,p.com_name
    context          = {}
    context['title'] = '公司'
    return render(request, 'predictCom.html', context)



def dataImport(request):
    return render(request, 'dataImport.html')


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

def dataSearch(request):
    context          = {}
    context['title'] = '数据查询'
    return render(request, 'dataSearch.html', context)

def test(request):
    context          = {}
    return render(request, 'testimport.html', context)