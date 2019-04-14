# -*- coding: utf-8 -*-
 
#from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import *

import copy
from Web.models import ZfjcCompanyBaseInfoDist
from Web.models import ZfjcCompanyFinanceInfo
from Web.models import EnvCompanyBaseInfo

regionCode = {'浦东':'01', '黄浦':'02', '静安':'03', '徐汇':'04', '长宁':'05', '普陀':'06', '虹口':'07', '杨浦':'08', '宝山':'09', '闵行':'10',
            '嘉定':'11', '金山':'12', '松江':'13','青浦':'14','奉贤':'15','崇明':'16'}

 
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
    #import copy
    #from Web.models import ZfjcCompanyBaseInfoRegionDist
    #print('aaaaa', request.POST.get('a'))
    region = request.POST.get('region') 
    selectRegion = request.POST.get('region')
    selectTime = request.POST.get('time')
    selectIndust = request.POST.get('industType')
    print('region', region)
    print('type', selectIndust)
    if selectIndust == None:
        selectIndust = '0'
    if selectTime == None:
        selectTime = '2017'
    regionCode = {'浦东': '01', '黄浦': '02', '静安': '03', '徐汇': '04', '长宁': '05', '普陀': '06', '虹口': '07', '杨浦': '08',
                 '宝山': '09', '闵行': '10', '嘉定': '11', '金山': '12', '松江': '13', '青浦': '14', '奉贤': '15', '崇明': '16'}
    region2Code = {'浦东': '01', '黄浦': '02', '静安': '03', '徐汇': '04', '长宁': '05', '普陀': '06', '虹口': '07', '杨浦': '08',
                 '宝山': '09', '闵行': '10', '嘉定': '11', '金山': '12', '松江': '13', '青浦': '14', '奉贤': '15', '崇明': '16'}
    code2Region = {}
    for r in regionCode:
        code2Region[regionCode[r]] = r
    regionList = ['浦东', '黄浦', '静安', '徐汇', '长宁', '普陀', '虹口', '杨浦',
                 '宝山', '闵行', '嘉定', '金山', '松江', '青浦', '奉贤', '崇明']
    regionCodeList = ['01', '02', '03', '04', '05', '06', '07', '08',
                  '09', '10', '11', '12', '13', '14', '15', '16']

    regionFilter = []
    industFilter = []
    legendData = []
    yAxisData = []

    if selectRegion == '0':
        yAxisData = regionList
        regionFilter = copy.deepcopy(regionCodeList)
        for i in range(len(regionFilter)):
            regionFilter[i] = 'shsqjd,' + regionFilter[i] + ','
    else:
        yAxisData = [code2Region[selectRegion]]
        regionFilter = ['shsqjd,' + region +',']

    if selectIndust == '0':
        legendData = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I','J']  # , 'K','L','M', 'N', 'O', 'P', 'Q', 'R', 'S']
        industFilter = copy.deepcopy(legendData)
        for i in range(len(industFilter)):
            industFilter[i] = 'gjjjhyfl,' + industFilter[i] + ','
    else:
        legendData = [selectIndust]
        industFilter = ['gjjjhyfl,' + selectIndust + ',']

    regionInfo = ZfjcCompanyBaseInfoRegionDist.objects.filter(region__in=regionFilter)
    print('filter result ', len(regionInfo))
    regionInfo1 = regionInfo.filter(industry_type__in=industFilter).filter(year=selectTime)
    print('filter result 1', len(regionInfo1))


    seriesData = [[0.0] * len(regionFilter) for i in range(len(industFilter))]
    for r in regionInfo1:
        regionId = r.region
        industryType = r.industry_type
        companyNum = r.company_num
        index2 = regionFilter.index(regionId)
        index1 = industFilter.index(industryType)
        seriesData[index1][index2] = companyNum

    d = {'legendData': legendData, 'yAxisData': yAxisData,
         'seriesData': seriesData}
    print(seriesData)
    print('legendData', legendData)
    print('yaxis', yAxisData)

    return HttpResponse(json.dumps(d), content_type='application/json')


def govPolicyRegionComCapital(request):
    #print('aaaaa', request.POST.get('a'))
    region = request.POST.get('region')
    #print('region', region)
    if region == '0':
        #import copy
        # from Web.models import ZfjcCompanyBaseInfoRegionDist

        regionCode = {'浦东': '01', '黄浦': '02', '静安': '03', '徐汇': '04', '长宁': '05', '普陀': '06', '虹口': '07', '杨浦': '08',
                      '宝山': '09', '闵行': '10', '嘉定': '11', '金山': '12', '松江': '13', '青浦': '14', '奉贤': '15', '崇明': '16'}
        for r in regionCode:
            regionCode[r] = 'shsqjd,' + regionCode[r] + ','

        regionNames = list(regionCode.keys())
        regionIds = list(regionCode.values())

        yAxisData = regionNames
        #industryTypes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K','L','M', 'N', 'O', 'P', 'Q', 'R', 'S']
        industryTypes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I','J']  # , 'K','L','M', 'N', 'O', 'P', 'Q', 'R', 'S']
        legendData = copy.deepcopy(industryTypes)
        for i in range(len(industryTypes)):
            industryTypes[i] = 'gjjjhyfl,' + industryTypes[i] + ','

        regionInfo = ZfjcCompanyBaseInfoRegionDist.objects.filter(region__in=regionIds)
        #print(regionIds)
        #print(regionInfo)
        regionInfo1 = regionInfo.filter(industry_type__in=industryTypes).filter(
            year=2017)

        #seriesData = [[0.0] * len(industryTypes) for i in range(len(regionIds))]
        seriesData = [[0.0] * len(regionIds) for i in range(len(industryTypes))]

        for r in regionInfo1:
            regionId = r.region
            industryType = r.industry_type
            capital = r.register_capital
            index2 = regionIds.index(regionId)
            index1 = industryTypes.index(industryType)
            seriesData[index1][index2] = capital/10000.0

        #print('series data capital', seriesData)

        d = {'legendData': legendData, 'yAxisData': yAxisData,
             'seriesData': seriesData}

    return HttpResponse(json.dumps(d), content_type='application/json')


def govPolicyRegionComTaxRelief(request):
    #print('aaaaa', request.POST.get('a'))
    region = request.POST.get('region')
    #print('taxRelief')
    #print('region', region)
    d = {}
    if region == '0':
        #print('taxRelief')
        # import copy
        # from Web.models import ZfjcCompanyBaseInfoRegionDist

        regionCode = {'浦东': '01', '黄浦': '02', '静安': '03', '徐汇': '04', '长宁': '05', '普陀': '06', '虹口': '07', '杨浦': '08',
                      '宝山': '09', '闵行': '10', '嘉定': '11', '金山': '12', '松江': '13', '青浦': '14', '奉贤': '15', '崇明': '16'}
        for r in regionCode:
            regionCode[r] = 'shsqjd,' + regionCode[r] + ','

        regionNames = list(regionCode.keys())
        regionIds = list(regionCode.values())

        yAxisData = regionNames
        #industryTypes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K','L','M', 'N', 'O', 'P', 'Q', 'R', 'S']
        industryTypes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I','J']  # , 'K','L','M', 'N', 'O', 'P', 'Q', 'R', 'S']
        legendData = copy.deepcopy(industryTypes)
        for i in range(len(industryTypes)):
            industryTypes[i] = 'gjjjhyfl,' + industryTypes[i] + ','

        regionInfo = ZfjcCompanyBaseInfoRegionDist.objects.filter(region__in=regionIds)
        #print(regionIds)
        #print(regionInfo)
        regionInfo1 = regionInfo.filter(industry_type__in=industryTypes).filter(
            year=2017)

        #seriesData = [[0.0] * len(industryTypes) for i in range(len(regionIds))]
        seriesData = [[0.0] * len(regionIds) for i in range(len(industryTypes))]
        regionSum = [0.0] * len(regionIds)
        

        for r in regionInfo1:
            regionId = r.region
            industryType = r.industry_type
            tax_relief = r.total_relief_tax/10000
            index2 = regionIds.index(regionId)
            index1 = industryTypes.index(industryType)
            regionSum[index2] += tax_relief
            seriesData[index1][index2] = tax_relief

        #print('series data capital', seriesData)
        #print('regionSum', regionSum)

        d = {'legendData': legendData, 'yAxisData': yAxisData,
             'seriesData': seriesData, 'regionSum': regionSum, 'test':'a'}
        return HttpResponse(json.dumps(d), content_type='application/json')

def govPolicyRegionComIncom(request):
    #print('aaaaa', request.POST.get('a'))
    region = request.POST.get('region')
    #print('taxRelief')
    #print('region', region)
    d = {}
    if region == '0':
        # import copy
        # from Web.models import ZfjcCompanyBaseInfoRegionDist

        regionCode = {'浦东': '01', '黄浦': '02', '静安': '03', '徐汇': '04', '长宁': '05', '普陀': '06', '虹口': '07', '杨浦': '08',
                      '宝山': '09', '闵行': '10', '嘉定': '11', '金山': '12', '松江': '13', '青浦': '14', '奉贤': '15', '崇明': '16'}
        for r in regionCode:
            regionCode[r] = 'shsqjd,' + regionCode[r] + ','

        regionNames = list(regionCode.keys())
        regionIds = list(regionCode.values())

        yAxisData = regionNames
        #industryTypes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K','L','M', 'N', 'O', 'P', 'Q', 'R', 'S']
        industryTypes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I','J']  # , 'K','L','M', 'N', 'O', 'P', 'Q', 'R', 'S']
        legendData = copy.deepcopy(industryTypes)
        for i in range(len(industryTypes)):
            industryTypes[i] = 'gjjjhyfl,' + industryTypes[i] + ','

        regionInfo = ZfjcCompanyBaseInfoRegionDist.objects.filter(region__in=regionIds)
        #print(regionIds)
        #print(regionInfo)
        regionInfo1 = regionInfo.filter(industry_type__in=industryTypes).filter(
            year=2017)

        #seriesData = [[0.0] * len(industryTypes) for i in range(len(regionIds))]
        seriesData = [[0.0] * len(regionIds) for i in range(len(industryTypes))]
        regionSum = [0.0] * len(regionIds)
        

        for r in regionInfo1:
            regionId = r.region
            industryType = r.industry_type
            total_incom = r.total_income/10000
            index2 = regionIds.index(regionId)
            index1 = industryTypes.index(industryType)
            regionSum[index2] += total_incom
            seriesData[index1][index2] = total_incom

        #print('series data capital', seriesData)
        #print('regionSum', regionSum)

        d = {'legendData': legendData, 'yAxisData': yAxisData,
             'seriesData': seriesData, 'regionSum': regionSum, 'test':'a'}
        return HttpResponse(json.dumps(d), content_type='application/json')

def govPolicyRegionComIncrease(request):
    region = request.POST.get('region')
    d = {}
    if region == '0':
        # import copy
        # from Web.models import ZfjcCompanyBaseInfoRegionDist

        regionCode = {'浦东': '01', '黄浦': '02', '静安': '03', '徐汇': '04', '长宁': '05', '普陀': '06', '虹口': '07', '杨浦': '08',
                      '宝山': '09', '闵行': '10', '嘉定': '11', '金山': '12', '松江': '13', '青浦': '14', '奉贤': '15', '崇明': '16'}
        for r in regionCode:
            regionCode[r] = 'shsqjd,' + regionCode[r] + ','

        regionNames = list(regionCode.keys())
        regionIds = list(regionCode.values())

        yAxisData = regionNames
        #industryTypes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K','L','M', 'N', 'O', 'P', 'Q', 'R', 'S']
        industryTypes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I','J']  # , 'K','L','M', 'N', 'O', 'P', 'Q', 'R', 'S']
        legendData = copy.deepcopy(industryTypes)
        for i in range(len(industryTypes)):
            industryTypes[i] = 'gjjjhyfl,' + industryTypes[i] + ','

        regionInfo = ZfjcCompanyBaseInfoRegionDist.objects.filter(region__in=regionIds)
        regionInfo1 = regionInfo.filter(industry_type__in=industryTypes).filter(
            year__in=[2017, 2016])

        seriesData1 = [[0.0] * len(regionIds) for i in range(len(industryTypes))]
        regionSum1 = [0.0] * len(regionIds)

        seriesData2 = [[0.0] * len(regionIds) for i in range(len(industryTypes))]
        regionSum2 = [0.0] * len(regionIds)
        

        for r in regionInfo1:
            regionId = r.region
            industryType = r.industry_type
            total_incom = r.total_income
            yearTime = r.year
            index2 = regionIds.index(regionId)
            index1 = industryTypes.index(industryType)
            if yearTime == '2016' or yearTime == 2016:
                regionSum1[index2] += total_incom
                seriesData1[index1][index2] = total_incom
            else:
                regionSum2[index2] += total_incom
                seriesData2[index1][index2] = total_incom

        seriesData = [[0.0] * len(regionIds) for i in range(len(industryTypes))]
        regionSum = [0.0] * len(regionIds)

        for i in range(len(regionIds)):
            if regionSum1[i] > 0 and regionSum2[i] > 0:
                regionSum[i] = (regionSum1[i]- regionSum1[i])/regionSum1[i]
            else:
                regionSum[i] = 0.0
            for j in range(len(industryTypes)):
                if seriesData1[j][i]>0 and seriesData2[j][i]>0:
                    seriesData[j][i] = (seriesData2[j][i]-seriesData1[j][i])/seriesData1[j][i]
                else:
                    seriesData[j][i] = 0.0

        regionSumMin = [0.0] * len(regionIds)
        regionSumMax = [0.0] * len(regionIds)
        for i in range(len(regionIds)):
            for j in range(len(industryTypes)):
                if seriesData[j][i] > regionSumMax[i]:
                    regionSumMax[i] = seriesData[j][i]
                if seriesData[j][i] < regionSumMin[i]:
                    regionSumMin[i] = seriesData[j][i]


        d = {'legendData': legendData, 'yAxisData': yAxisData,
             'seriesData': seriesData, 'regionSum': regionSum,'regionSumMin': regionSumMin,'regionSumMax': regionSumMax}
        return HttpResponse(json.dumps(d), content_type='application/json')



def govPolicyTimeView(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'govPolicyMacroTime.html', context)

def govPolicyTimeRegionInfoQuery(request):
    # import copy
    # from Web.models import ZfjcCompanyBaseInfoDist
    # from Web.models import ZfjcCompanyFinanceInfo
    # from Web.models import EnvCompanyBaseInfo

    region2Code = {'浦东': '01', '黄浦': '02', '静安': '03', '徐汇': '04', '长宁': '05', '普陀': '06', '虹口': '07', '杨浦': '08',
                   '宝山': '09', '闵行': '10', '嘉定': '11', '金山': '12', '松江': '13', '青浦': '14', '奉贤': '15', '崇明': '16'}
    code2Region = {}
    for r in regionCode:
        code2Region[regionCode[r]] = r

    regionList = ['浦东', '黄浦', '静安', '徐汇', '长宁', '普陀', '虹口', '杨浦',
                 '宝山', '闵行', '嘉定', '金山', '松江', '青浦', '奉贤', '崇明']
    regionCodeList = ['01', '02', '03', '04', '05', '06', '07', '08',
                  '09', '10', '11', '12', '13', '14', '15', '16']

    timeMin = request.POST.get('selectTimeMin')
    timeMax = request.POST.get('selectTimeMax')
    selectRegion = request.POST.get('selectRegion')
    selectIndust = request.POST.get('selectIndust')

    if selectRegion == '0':
        regionFilter = copy.deepcopy(regionCodeList)
        for i in range(len(regionFilter)):
            regionFilter[i] = 'shsqjd,' + regionFilter[i] + ','
    else:
        xAxisData = [code2Region[selectRegion]]
        regionFilter = ['shsqjd,' + region +',']

    if selectIndust == '0':
        legendData = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I','J']  # , 'K','L','M', 'N', 'O', 'P', 'Q', 'R', 'S']
        industFilter = copy.deepcopy(legendData)
        for i in range(len(industFilter)):
            industFilter[i] = 'gjjjhyfl,' + industFilter[i] + ','
    else:
        legendData = [selectIndust]
        industFilter = ['gjjjhyfl,' + selectIndust + ',']

    regionInfo = ZfjcCompanyBaseInfoRegionDist.objects.filter(region__in=regionFilter)
    regionInfo = regionInfo.filter(industry_type__in=industFilter)
    timeMin = int(timeMin)
    timeMax = int(timeMax)
    regionInfo = regionInfo.filter(year__gte=timeMin).filter(year__lte=timeMax)
    xAxisData = []
    for i in range(timeMin, timeMax+1):
        xAxisData.append(i)


    taxReliefSData = [[0.0]*(timeMax-timeMin+1) for i in range(len(legendData))]
    incomeSData = [[0.0]*(timeMax-timeMin+1) for i in range(len(legendData))]
    increaseSData = [[0.0]*(timeMax-timeMin+1) for i in range(len(legendData))]
    for r in regionInfo:
        regionId = r.region
        industryType = r.industry_type
        total_relief_tax = r.total_relief_tax
        total_income = r.total_income
        total_increase_value = r.total_increase_value
        infoYear = r.year
        index1 = industFilter.index(industryType)
        index2 = xAxisData.index(infoYear)
        taxReliefSData[index1][index2] = total_relief_tax
        incomeSData[index1][index2] = total_income
        increaseSData[index1][index2] = total_increase_value

    d = {'legendData': legendData, 'xAxisData': xAxisData,'taxReliefSData':taxReliefSData,'incomeSData':incomeSData, 'increaseSData':increaseSData}
    return HttpResponse(json.dumps(d), content_type='application/json')

def govPolicyTimeRegionInfoCompare(request):
    region2Code = {'浦东': '01', '黄浦': '02', '静安': '03', '徐汇': '04', '长宁': '05', '普陀': '06', '虹口': '07', '杨浦': '08',
                   '宝山': '09', '闵行': '10', '嘉定': '11', '金山': '12', '松江': '13', '青浦': '14', '奉贤': '15', '崇明': '16'}
    code2Region = {}
    for r in regionCode:
        code2Region[regionCode[r]] = r

    regionList = ['浦东', '黄浦', '静安', '徐汇', '长宁', '普陀', '虹口', '杨浦',
                 '宝山', '闵行', '嘉定', '金山', '松江', '青浦', '奉贤', '崇明']
    regionCodeList = ['01', '02', '03', '04', '05', '06', '07', '08',
                  '09', '10', '11', '12', '13', '14', '15', '16']

    selectTime1 = request.POST.get('selectTime1')
    selectTime2 = request.POST.get('selectTime2')
    selectRegion = request.POST.get('selectRegion')
    selectIndust = request.POST.get('selectIndust')

    xAxisData = []
    if selectRegion == '0':
        xAxisData = regionList
        regionFilter = copy.deepcopy(regionCodeList)
        for i in range(len(regionFilter)):
            regionFilter[i] = 'shsqjd,' + regionFilter[i] + ','
    else:
        xAxisData = [code2Region[selectRegion]]
        regionFilter = ['shsqjd,' + selectRegion +',']

    if selectIndust == '0':
        legendData = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I','J']  # , 'K','L','M', 'N', 'O', 'P', 'Q', 'R', 'S']
        industFilter = copy.deepcopy(legendData)
        for i in range(len(industFilter)):
            industFilter[i] = 'gjjjhyfl,' + industFilter[i] + ','
    else:
        legendData = [selectIndust]
        industFilter = ['gjjjhyfl,' + selectIndust + ',']

    regionInfo = ZfjcCompanyBaseInfoRegionDist.objects.filter(region__in=regionFilter)
    regionInfo = regionInfo.filter(industry_type__in=industFilter)
    selectTime1 = int(selectTime1)
    selectTime2 = int(selectTime2)
    regionInfo = regionInfo.filter(year__in=[selectTime1, selectTime2])

    taxReliefSData1 = [[0.0]*len(regionFilter) for i in range(len(legendData))]
    incomeSData1 = [[0.0]*len(regionFilter) for i in range(len(legendData))]
    increaseSData1 = [[0.0]*len(regionFilter) for i in range(len(legendData))]
    taxReliefSData2 = [[0.0]*len(regionFilter) for i in range(len(legendData))]
    incomeSData2 = [[0.0]*len(regionFilter) for i in range(len(legendData))]
    increaseSData2 = [[0.0]*len(regionFilter) for i in range(len(legendData))]
    for r in regionInfo:
        regionId = r.region
        industryType = r.industry_type
        total_relief_tax = r.total_relief_tax
        total_income = r.total_income
        total_increase_value = r.total_increase_value
        infoYear = r.year
        index1 = industFilter.index(industryType)
        index2 = regionFilter.index(regionId)
        if infoYear == selectTime1:
            taxReliefSData1[index1][index2] = total_relief_tax
            incomeSData1[index1][index2] = total_income
            increaseSData1[index1][index2] = total_increase_value
        if infoYear == selectTime2:
            taxReliefSData2[index1][index2] = total_relief_tax
            incomeSData2[index1][index2] = total_income
            increaseSData2[index1][index2] = total_increase_value
    print('increase Sdata', increaseSData1)

    d = {'legendData': legendData, 'xAxisData': xAxisData,'taxReliefSData1':taxReliefSData1,'incomeSData1':incomeSData1, 'increaseSData1':increaseSData1,
         'taxReliefSData2':taxReliefSData2,'incomeSData2':incomeSData2, 'increaseSData2':increaseSData2}
    return HttpResponse(json.dumps(d), content_type='application/json')

def govPolicyBusinessView(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'govPolicyMacroBusiness.html', context)

def govPolicyComView(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'govPolicyMicroCom.html', context)

def govPolicyComInfo(request):
    # import copy
    # from Web.models import ZfjcCompanyBaseInfoDist
    # from Web.models import ZfjcCompanyFinanceInfo

    region2Code = {'浦东': '01', '黄浦': '02', '静安': '03', '徐汇': '04', '长宁': '05', '普陀': '06', '虹口': '07', '杨浦': '08',
                 '宝山': '09', '闵行': '10', '嘉定': '11', '金山': '12', '松江': '13', '青浦': '14', '奉贤': '15', '崇明': '16'}
    code2Region = {}
    for r in regionCode:
        code2Region[regionCode[r]] = r

    selectRegion = request.POST.get('region')
    selectTime = request.POST.get('time')
    selectIndust = request.POST.get('industType')
    searchComName = request.POST.get('searchComName')
    print(selectRegion, selectTime, selectIndust, searchComName)
    regionInfo = ZfjcCompanyBaseInfoDist.objects.all()
    if selectRegion != '0':
        regionInfo = regionInfo.filter(region__contains=selectRegion)
    if selectTime != '0':
        regionInfo = regionInfo.filter(register_date__contains=selectTime)
    if selectIndust != '0':
        regionInfo = regionInfo.filter(industry_type='gjjjhyfl,' + selectIndust + ',')
    if searchComName != '':
        regionInfo = regionInfo.filter(company_name__contains=searchComName)

    comList = []
    imax = 10
    for c in regionInfo:
        comId = c.company_id
        comName = c.company_name
        region = c.region
        if region != None and region!='None' and region!=''and region!=' ':
            print(region)
            rCode = region[-3:-1]
            comList.append([comId, comName, code2Region[rCode]])
        else:
            comList.append([comId, comName, ''])
        if len(comList) > imax:
            break
    print(comList)
    d = {'comInfo':comList}
    return HttpResponse(json.dumps(d), content_type='application/json')

def govPolicyComFinance(request):
    # import copy
    # from Web.models import ZfjcCompanyBaseInfoDist
    # from Web.models import ZfjcCompanyFinanceInfo
    # from Web.models import EnvCompanyBaseInfo

    region2Code = {'浦东': '01', '黄浦': '02', '静安': '03', '徐汇': '04', '长宁': '05', '普陀': '06', '虹口': '07', '杨浦': '08',
                   '宝山': '09', '闵行': '10', '嘉定': '11', '金山': '12', '松江': '13', '青浦': '14', '奉贤': '15', '崇明': '16'}
    code2Region = {}
    for r in regionCode:
        code2Region[regionCode[r]] = r

    comIdList = json.loads(request.POST.get('comIdList'))
    timeMin = request.POST.get('timeMin')
    timeMax = request.POST.get('timeMax')
    #print(comIdList, timeMin, timeMax)
    regionInfo = EnvCompanyBaseInfo.objects.all()
    regionInfo = regionInfo.filter(company_id__in=comIdList)
    regionInfo = regionInfo.filter(year__gte=timeMin).filter(year__lte=timeMax)

    comNameList = ['']*len(comIdList)
    #print('length of comIdList', comIdList)
    #print('length of comIdList', len(comIdList))
    timeMin = int(timeMin)
    timeMax = int(timeMax)
    financeIdDic = {}
    for c in regionInfo:
        fianceId = c.id

        comId = str(c.company_id)
        comName = c.company_name
        rTime = c.year

        index1 = comIdList.index(comId)
        if comNameList[index1] == '':
            comNameList[index1] = comName
        index2 = int(rTime)-timeMin
        financeIdDic[fianceId] = [comId, comName, index1, index2]

    totalIncomeData = [[0.0]*(timeMax-timeMin+1) for i in range(len(comIdList))]
    totalReliefData = [[0.0] * (timeMax - timeMin + 1) for i in range(len(comIdList))]
    totalIncreaseData = [[0.0] * (timeMax - timeMin + 1) for i in range(len(comIdList))]
    financeIdList = financeIdDic.keys()
    regionInfo = ZfjcCompanyFinanceInfo.objects.filter(id__in=financeIdList)
    print('regionInfo length', len(regionInfo))
    for c in regionInfo:
        financeId = c.id
        total_income = c.total_income
        total_relief_tax = c.total_relief_tax
        total_increase_value = c.total_increase_value
        cInfo = financeIdDic[financeId]
        index1 = cInfo[2]
        index2 = cInfo[3]
        if total_income != '' and total_income != None:
            totalIncomeData[index1][index2] = total_income
        if total_relief_tax != '' and total_relief_tax != None:
            totalReliefData[index1][index2] = total_relief_tax
        if total_increase_value != '' and total_increase_value != None:
            totalIncreaseData[index1][index2] = total_increase_value
    yearList = []
    for y in range(timeMin, timeMax+1):
        yearList.append(y)
    print(comNameList, yearList, totalIncomeData)
    d = {'comNameList': comNameList, 'yearList': yearList,'totalIncomeData': totalIncomeData,'totalReliefData':totalReliefData,'totalIncreaseData':totalIncreaseData}
    return HttpResponse(json.dumps(d), content_type='application/json')

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

