#!/usr/bin/env python
#coding:utf-8
  
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SataWebServer.settings")

  
'''
Django 版本大于等于1.7的时候，需要加上下面两句
import django
django.setup()
否则会抛出错误 django.core.exceptions.AppRegistryNotReady: Models aren't loaded yet.
'''
  
import django
if django.VERSION >= (1, 7):#自动判断版本
    django.setup()

def testRegion():
    # from Web.models import ZfjcCompanyBaseInfoRegionDist
    # regionInfo = ZfjcCompanyBaseInfoRegionDist.objects.filter(region__in = ['shsqjd,01,','shsqjd,02,','shsqjd,03,'])
    # regionInfo1 = regionInfo.filter(industry_type__in = ['gjjjhyfl,A,','gjjjhyfl,B,', 'gjjjhyfl,C,']).filter(year=2017)
    #
    # #mydata = ZfjcCompanyBaseInfoRegionDist.objects.all()
    # #print(mydata)
    #
    #
    # legendData = ['A', 'B', 'C']
    # yAxisData = ['浦东', '黄浦', '静安']
    # regionIds = ['shsqjd,01,','shsqjd,02,','shsqjd,03,']
    # industryTypes = ['gjjjhyfl,A,', 'gjjjhyfl,B,', 'gjjjhyfl,C,']
    # seriesData = [[0.0] * 3 for i in range(3)]
    #
    #
    #
    # for r in regionInfo1:
    #     regionId = r.region
    #     industryType = r.industry_type
    #     companyNum = r.company_num
    #     index1 = regionIds.index(regionId)
    #     index2 = industryTypes.index(industryType)
    #     seriesData[index1][index2] = companyNum
    #
    #
    # print(seriesData)
    # #print(type(r.company_num))
    #
    # d = {'legendData': legendData, 'yAxisData': yAxisData,
    #      'seriesData': seriesData}
    #
    # # for r in regionInfo1:
    # #     print(r.company_num)
    # #     print(type(r.company_num))
    #


    #================
    import copy
    regionCode = {'浦东': '01', '黄浦': '02', '静安': '03', '徐汇': '04', '长宁': '05', '普陀': '06', '虹口': '07', '杨浦': '08',
                  '宝山': '09', '闵行': '10', '嘉定': '11', '金山': '12', '松江': '13', '青浦': '14', '奉贤': '15', '崇明': '16'}
    for r in regionCode:
        regionCode[r] = 'shsqjd,' + regionCode[r] + ','

    regionNames = list(regionCode.keys())
    regionIds = list(regionCode.values())

    yAxisData = regionNames
    # industryTypes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K','L','M', 'N', 'O', 'P', 'Q', 'R', 'S']
    industryTypes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']  # , 'K','L','M', 'N', 'O', 'P', 'Q', 'R', 'S']
    legendData = copy.deepcopy(industryTypes)
    for i in range(len(industryTypes)):
        industryTypes[i] = 'gjjjhyfl,' + industryTypes[i] + ','

    # d = {'legendData':['A','B','C'], 'yAxisData':['浦东','黄浦','静安'],'seriesData':[[320, 302, 301], [334, 390, 330], [120, 132, 101]]}

    from Web.models import ZfjcCompanyBaseInfoRegionDist
    regionInfo = ZfjcCompanyBaseInfoRegionDist.objects.filter(region__in=regionIds)
    print(regionIds)
    print(regionInfo)
    regionInfo1 = regionInfo.filter(industry_type__in=industryTypes).filter(
        year=2017)

    # legendData = ['A', 'B', 'C']
    # yAxisData = ['浦东', '黄浦', '静安']
    # regionIds = ['shsqjd,01,', 'shsqjd,02,', 'shsqjd,03,']
    # industryTypes = ['gjjjhyfl,A,', 'gjjjhyfl,B,', 'gjjjhyfl,C,']
    seriesData = [[0.0] * len(industryTypes) for i in range(len(regionIds))]

    for r in regionInfo1:
        regionId = r.region
        industryType = r.industry_type
        companyNum = r.company_num
        index1 = regionIds.index(regionId)
        index2 = industryTypes.index(industryType)
        seriesData[index1][index2] = companyNum

    print(seriesData)
    # print(type(r.company_num))

    d = {'legendData': legendData, 'yAxisData': yAxisData,
         'seriesData': seriesData}


def govPolicyRegionComTaxRelief():
    import copy
    from Web.models import ZfjcCompanyBaseInfoRegionDist

    regionCode = {'浦东': '01', '黄浦': '02', '静安': '03', '徐汇': '04', '长宁': '05', '普陀': '06', '虹口': '07', '杨浦': '08',
                  '宝山': '09', '闵行': '10', '嘉定': '11', '金山': '12', '松江': '13', '青浦': '14', '奉贤': '15', '崇明': '16'}
    for r in regionCode:
        regionCode[r] = 'shsqjd,' + regionCode[r] + ','

    regionNames = list(regionCode.keys())
    regionIds = list(regionCode.values())

    yAxisData = regionNames
    # industryTypes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K','L','M', 'N', 'O', 'P', 'Q', 'R', 'S']
    industryTypes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
                     'J']  # , 'K','L','M', 'N', 'O', 'P', 'Q', 'R', 'S']
    legendData = copy.deepcopy(industryTypes)
    for i in range(len(industryTypes)):
        industryTypes[i] = 'gjjjhyfl,' + industryTypes[i] + ','

    regionInfo = ZfjcCompanyBaseInfoRegionDist.objects.filter(region__in=regionIds)
    #print(regionIds)
    #print(regionInfo)
    regionInfo1 = regionInfo.filter(industry_type__in=industryTypes).filter(
        year=2017)

    # seriesData = [[0.0] * len(industryTypes) for i in range(len(regionIds))]
    seriesData = [[0.0] * len(regionIds) for i in range(len(industryTypes))]
    regionSum = [0.0] * len(regionIds)

    for r in regionInfo1:
        regionId = r.region
        industryType = r.industry_type
        tax_relief = r.total_relief_tax
        index2 = regionIds.index(regionId)
        index1 = industryTypes.index(industryType)
        regionSum[index2] += tax_relief
        seriesData[index1][index2] = tax_relief

    #print('series data capital', seriesData)
    print('regionSum', regionSum)

    d = {'legendData': legendData, 'yAxisData': yAxisData,
         'seriesData': seriesData, 'regionSum': regionSum, 'test': 'a'}

  
def main():
    #testRegion()
    govPolicyRegionComTaxRelief()
	#from Web.models import EnvCompanyBaseInfo

    #list = EnvCompanyBaseInfo.objects.all()
    #print(list)
    #print('number of results:', len(list))

#    f = open('oldblog.txt')
#    for line in f:
#        title,content = line.split('****')
#        Blog.objects.create(title=title,content=content)
#    f.close()
  
if __name__ == "__main__":
    main()
    print('Done!')