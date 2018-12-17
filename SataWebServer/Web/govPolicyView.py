# -*- coding: utf-8 -*-
 
#from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import *
import copy

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
    import copy
    from Web.models import ZfjcCompanyBaseInfoRegionDist
    #print('aaaaa', request.POST.get('a'))
    region = request.POST.get('region') 
    selectTime = request.POST.get('time')
    selectIndust = request.POST.get('industType')
    #print('region', region)
    if region == '0':
        regionCode = {'浦东': '01', '黄浦': '02', '静安': '03', '徐汇': '04', '长宁': '05', '普陀': '06', '虹口': '07', '杨浦': '08',
                      '宝山': '09', '闵行': '10',
                      '嘉定': '11', '金山': '12', '松江': '13', '青浦': '14', '奉贤': '15', '崇明': '16'}
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
            companyNum = r.company_num
            index2 = regionIds.index(regionId)
            index1 = industryTypes.index(industryType)
            seriesData[index1][index2] = companyNum

        #print('series data', seriesData)

        d = {'legendData': legendData, 'yAxisData': yAxisData,
             'seriesData': seriesData}
    else:
        regionIds = ['shsqjd,' + region +',']
        #selectTime = request.POST.get('time')
        industryTypes = []
        if selectIndust == '0':
            #industryTypes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K','L','M', 'N', 'O', 'P', 'Q', 'R', 'S']
            industryTypes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I','J']  # , 'K','L','M', 'N', 'O', 'P', 'Q', 'R', 'S']
            legendData = copy.deepcopy(industryTypes)
            for i in range(len(industryTypes)):
                industryTypes[i] = 'gjjjhyfl,' + industryTypes[i] + ','
        else:
            industryTypes = ['gjjjhyfl,' + selectIndust + ',']

        regionInfo = ZfjcCompanyBaseInfoRegionDist.objects.filter(region__in=regionIds)
        regionInfo1 = regionInfo.filter(industry_type__in=[selectIndust]).filter(year=selectTime)

        seriesData =[[0.0] * len(regionIds) for i in range(len(selectIndust))]
        yAxisData = regionIds
        legendData = industryTypes

        for r in regionInfo1:
            regionId = r.region
            industryType = r.industry_type
            companyNum = r.company_num
            index2 = regionIds.index(regionId)
            index1 = industryTypes.index(industryType)
            seriesData[index1][index2] = companyNum

        #print('series data', seriesData)

        d = {'legendData': legendData, 'yAxisData': yAxisData,
             'seriesData': seriesData}


    return HttpResponse(json.dumps(d), content_type='application/json')

def govPolicyRegionComCapital(request):
    #print('aaaaa', request.POST.get('a'))
    region = request.POST.get('region')
    #print('region', region)
    if region == '0':
        import copy
        from Web.models import ZfjcCompanyBaseInfoRegionDist

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
    print('taxRelief')
    #print('region', region)
    d = {}
    if region == '0':
        print('taxRelief')
        import copy
        from Web.models import ZfjcCompanyBaseInfoRegionDist

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
        print(regionIds)
        print(regionInfo)
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

        print('series data capital', seriesData)
        #print('regionSum', regionSum)

        d = {'legendData': legendData, 'yAxisData': yAxisData,
             'seriesData': seriesData, 'regionSum': regionSum, 'test':'a'}
        return HttpResponse(json.dumps(d), content_type='application/json')

def govPolicyRegionComIncom(request):
    #print('aaaaa', request.POST.get('a'))
    region = request.POST.get('region')
    print('taxRelief')
    #print('region', region)
    d = {}
    if region == '0':
        import copy
        from Web.models import ZfjcCompanyBaseInfoRegionDist

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
        print(regionIds)
        print(regionInfo)
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
        import copy
        from Web.models import ZfjcCompanyBaseInfoRegionDist

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