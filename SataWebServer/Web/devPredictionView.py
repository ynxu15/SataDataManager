# coding=utf-8
#from django.http import HttpResponse
from django.shortcuts import render
from django import forms
from django.template import RequestContext
from models import Eps,Jlr,Jsy
from django.db.models import Count,Avg
import json
from django.http import HttpResponse
from django.template import RequestContext, loader


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

    region_select = request.GET.get('region')
    type_select = request.GET.get('type')

    context['region_select'] = region_select
    context['type_select'] = type_select

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


def getByRegion(request):
    region = request.GET['region']
    
    Eps_region = Eps.objects.all().values('com_region').annotate(avg_001=Avg('pf_001'),avg_002=Avg('pf_002'),avg_003=Avg('pf_003'),avg_004=Avg('pf_004'),avg_011=Avg('pf_011'),avg_012=Avg('pf_012'),avg_013=Avg('pf_013'),avg_014=Avg('pf_014'),avg_021=Avg('pf_021'),avg_022=Avg('pf_022'),avg_023=Avg('pf_023'),avg_024=Avg('pf_024'),avg_031=Avg('pf_031'),avg_032=Avg('pf_032'),avg_033=Avg('pf_033'),avg_034=Avg('pf_034'),avg_041=Avg('pf_041'),avg_042=Avg('pf_042'),avg_043=Avg('pf_043'),avg_044=Avg('pf_044'),avg_051=Avg('pf_051'),avg_052=Avg('pf_052'),avg_053=Avg('pf_053'),avg_054=Avg('pf_054'),avg_061=Avg('pf_061'),avg_062=Avg('pf_062'),avg_063=Avg('pf_063'),avg_064=Avg('pf_064'),avg_071=Avg('pf_071'),avg_072=Avg('pf_072'),avg_073=Avg('pf_073'),avg_074=Avg('pf_074'),avg_081=Avg('pf_081'),avg_082=Avg('pf_082'),avg_083=Avg('pf_083'),avg_084=Avg('pf_084'),avg_091=Avg('pf_091'),avg_092=Avg('pf_092'),avg_093=Avg('pf_093'),avg_094=Avg('pf_094'),avg_101=Avg('pf_101'),avg_102=Avg('pf_102'),avg_103=Avg('pf_103'),avg_104=Avg('pf_104'),avg_111=Avg('pf_111'),avg_112=Avg('pf_112'),avg_113=Avg('pf_113'),avg_114=Avg('pf_114'),avg_121=Avg('pf_121'),avg_122=Avg('pf_122'),avg_123=Avg('pf_123'),avg_124=Avg('pf_124'),avg_131=Avg('pf_131'),avg_132=Avg('pf_132'),avg_133=Avg('pf_133'),avg_134=Avg('pf_134'),avg_141=Avg('pf_141'),avg_142=Avg('pf_142'),avg_143=Avg('pf_143'),avg_144=Avg('pf_144'),avg_151=Avg('pf_151'),avg_152=Avg('pf_152'),avg_153=Avg('pf_153'),avg_154=Avg('pf_154'),avg_161=Avg('pf_161'),avg_162=Avg('pf_162'),avg_163=Avg('pf_163'),avg_164=Avg('pf_164'),avg_171=Avg('pf_171'),avg_172=Avg('pf_172'),avg_173=Avg('pf_173'),avg_174=Avg('pf_174'),avg_181=Avg('pf_181'),avg_182=Avg('pf_182'),avg_183=Avg('pf_183')).values('com_region', 'avg_001','avg_002','avg_003','avg_004','avg_011','avg_012','avg_013','avg_014','avg_021','avg_022','avg_023','avg_024','avg_031','avg_032','avg_033','avg_034','avg_041','avg_042','avg_043','avg_044','avg_051','avg_052','avg_053','avg_054','avg_061','avg_062','avg_063','avg_064','avg_071','avg_072','avg_073','avg_074','avg_081','avg_082','avg_083','avg_084','avg_091','avg_092','avg_093','avg_094','avg_101','avg_102','avg_103','avg_104','avg_111','avg_112','avg_113','avg_114','avg_121','avg_122','avg_123','avg_124','avg_131','avg_132','avg_133','avg_134','avg_141','avg_142','avg_143','avg_144','avg_151','avg_152','avg_153','avg_154','avg_161','avg_162','avg_163','avg_164','avg_171','avg_172','avg_173','avg_174','avg_181','avg_182','avg_183')

    Jlr_region = Jlr.objects.all().values('com_region').annotate(avg_001=Avg('pf_001'),avg_002=Avg('pf_002'),avg_003=Avg('pf_003'),avg_004=Avg('pf_004'),avg_011=Avg('pf_011'),avg_012=Avg('pf_012'),avg_013=Avg('pf_013'),avg_014=Avg('pf_014'),avg_021=Avg('pf_021'),avg_022=Avg('pf_022'),avg_023=Avg('pf_023'),avg_024=Avg('pf_024'),avg_031=Avg('pf_031'),avg_032=Avg('pf_032'),avg_033=Avg('pf_033'),avg_034=Avg('pf_034'),avg_041=Avg('pf_041'),avg_042=Avg('pf_042'),avg_043=Avg('pf_043'),avg_044=Avg('pf_044'),avg_051=Avg('pf_051'),avg_052=Avg('pf_052'),avg_053=Avg('pf_053'),avg_054=Avg('pf_054'),avg_061=Avg('pf_061'),avg_062=Avg('pf_062'),avg_063=Avg('pf_063'),avg_064=Avg('pf_064'),avg_071=Avg('pf_071'),avg_072=Avg('pf_072'),avg_073=Avg('pf_073'),avg_074=Avg('pf_074'),avg_081=Avg('pf_081'),avg_082=Avg('pf_082'),avg_083=Avg('pf_083'),avg_084=Avg('pf_084'),avg_091=Avg('pf_091'),avg_092=Avg('pf_092'),avg_093=Avg('pf_093'),avg_094=Avg('pf_094'),avg_101=Avg('pf_101'),avg_102=Avg('pf_102'),avg_103=Avg('pf_103'),avg_104=Avg('pf_104'),avg_111=Avg('pf_111'),avg_112=Avg('pf_112'),avg_113=Avg('pf_113'),avg_114=Avg('pf_114'),avg_121=Avg('pf_121'),avg_122=Avg('pf_122'),avg_123=Avg('pf_123'),avg_124=Avg('pf_124'),avg_131=Avg('pf_131'),avg_132=Avg('pf_132'),avg_133=Avg('pf_133'),avg_134=Avg('pf_134'),avg_141=Avg('pf_141'),avg_142=Avg('pf_142'),avg_143=Avg('pf_143'),avg_144=Avg('pf_144'),avg_151=Avg('pf_151'),avg_152=Avg('pf_152'),avg_153=Avg('pf_153'),avg_154=Avg('pf_154'),avg_161=Avg('pf_161'),avg_162=Avg('pf_162'),avg_163=Avg('pf_163'),avg_164=Avg('pf_164'),avg_171=Avg('pf_171'),avg_172=Avg('pf_172'),avg_173=Avg('pf_173'),avg_174=Avg('pf_174'),avg_181=Avg('pf_181'),avg_182=Avg('pf_182'),avg_183=Avg('pf_183')).values('com_region', 'avg_001','avg_002','avg_003','avg_004','avg_011','avg_012','avg_013','avg_014','avg_021','avg_022','avg_023','avg_024','avg_031','avg_032','avg_033','avg_034','avg_041','avg_042','avg_043','avg_044','avg_051','avg_052','avg_053','avg_054','avg_061','avg_062','avg_063','avg_064','avg_071','avg_072','avg_073','avg_074','avg_081','avg_082','avg_083','avg_084','avg_091','avg_092','avg_093','avg_094','avg_101','avg_102','avg_103','avg_104','avg_111','avg_112','avg_113','avg_114','avg_121','avg_122','avg_123','avg_124','avg_131','avg_132','avg_133','avg_134','avg_141','avg_142','avg_143','avg_144','avg_151','avg_152','avg_153','avg_154','avg_161','avg_162','avg_163','avg_164','avg_171','avg_172','avg_173','avg_174','avg_181','avg_182','avg_183')

    Jsy_region = Jsy.objects.all().values('com_region').annotate(avg_001=Avg('pf_001'),avg_002=Avg('pf_002'),avg_003=Avg('pf_003'),avg_004=Avg('pf_004'),avg_011=Avg('pf_011'),avg_012=Avg('pf_012'),avg_013=Avg('pf_013'),avg_014=Avg('pf_014'),avg_021=Avg('pf_021'),avg_022=Avg('pf_022'),avg_023=Avg('pf_023'),avg_024=Avg('pf_024'),avg_031=Avg('pf_031'),avg_032=Avg('pf_032'),avg_033=Avg('pf_033'),avg_034=Avg('pf_034'),avg_041=Avg('pf_041'),avg_042=Avg('pf_042'),avg_043=Avg('pf_043'),avg_044=Avg('pf_044'),avg_051=Avg('pf_051'),avg_052=Avg('pf_052'),avg_053=Avg('pf_053'),avg_054=Avg('pf_054'),avg_061=Avg('pf_061'),avg_062=Avg('pf_062'),avg_063=Avg('pf_063'),avg_064=Avg('pf_064'),avg_071=Avg('pf_071'),avg_072=Avg('pf_072'),avg_073=Avg('pf_073'),avg_074=Avg('pf_074'),avg_081=Avg('pf_081'),avg_082=Avg('pf_082'),avg_083=Avg('pf_083'),avg_084=Avg('pf_084'),avg_091=Avg('pf_091'),avg_092=Avg('pf_092'),avg_093=Avg('pf_093'),avg_094=Avg('pf_094'),avg_101=Avg('pf_101'),avg_102=Avg('pf_102'),avg_103=Avg('pf_103'),avg_104=Avg('pf_104'),avg_111=Avg('pf_111'),avg_112=Avg('pf_112'),avg_113=Avg('pf_113'),avg_114=Avg('pf_114'),avg_121=Avg('pf_121'),avg_122=Avg('pf_122'),avg_123=Avg('pf_123'),avg_124=Avg('pf_124'),avg_131=Avg('pf_131'),avg_132=Avg('pf_132'),avg_133=Avg('pf_133'),avg_134=Avg('pf_134'),avg_141=Avg('pf_141'),avg_142=Avg('pf_142'),avg_143=Avg('pf_143'),avg_144=Avg('pf_144'),avg_151=Avg('pf_151'),avg_152=Avg('pf_152'),avg_153=Avg('pf_153'),avg_154=Avg('pf_154'),avg_161=Avg('pf_161'),avg_162=Avg('pf_162'),avg_163=Avg('pf_163'),avg_164=Avg('pf_164'),avg_171=Avg('pf_171'),avg_172=Avg('pf_172'),avg_173=Avg('pf_173'),avg_174=Avg('pf_174'),avg_181=Avg('pf_181'),avg_182=Avg('pf_182'),avg_183=Avg('pf_183')).values('com_region', 'avg_001','avg_002','avg_003','avg_004','avg_011','avg_012','avg_013','avg_014','avg_021','avg_022','avg_023','avg_024','avg_031','avg_032','avg_033','avg_034','avg_041','avg_042','avg_043','avg_044','avg_051','avg_052','avg_053','avg_054','avg_061','avg_062','avg_063','avg_064','avg_071','avg_072','avg_073','avg_074','avg_081','avg_082','avg_083','avg_084','avg_091','avg_092','avg_093','avg_094','avg_101','avg_102','avg_103','avg_104','avg_111','avg_112','avg_113','avg_114','avg_121','avg_122','avg_123','avg_124','avg_131','avg_132','avg_133','avg_134','avg_141','avg_142','avg_143','avg_144','avg_151','avg_152','avg_153','avg_154','avg_161','avg_162','avg_163','avg_164','avg_171','avg_172','avg_173','avg_174','avg_181','avg_182','avg_183')



    ret_eps = Eps_region.filter(com_region=region)[0]
    ret_jlr = Jlr_region.filter(com_region=region)[0]
    ret_jsy = Jsy_region.filter(com_region=region)[0]

    data = [[],[],[]]
    for i in range(0,19):
        for j in range(1,5):
            if i==18 and j==4: 
                break
            if i<10:
                index = 'avg_0'+str(i)+str(j)
                data[0].append(ret_eps[index])
                data[1].append(ret_jlr[index])
                data[2].append(ret_jsy[index])
            else:
                index = 'avg_'+str(i)+str(j)
                data[0].append(ret_eps[index])
                data[1].append(ret_jlr[index])
                data[2].append(ret_jsy[index])
    # print data
    change = [[],[],[]]
    for i in range(3):
        for j in range(len(data[i])-1):
            change[i].append(float('%.2f' %(data[i][j+1]-data[i][j])))

    changeToBar = [[[],[]],[[],[]],[[],[]]]
    for i in range(3):
        for j in range(len(change[i])):
            if change[i][j] >= 0:
                changeToBar[i][0].append(change[i][j])
                changeToBar[i][1].append('-')
            else:
                changeToBar[i][1].append(change[i][j])
                changeToBar[i][0].append('-')
                
    # print len(change[0])
    # print len(changeToBar[0][0])
    # print len(changeToBar[0][1])
    ret = {'data':data,'change':change,'changeToBar':changeToBar}
    return HttpResponse(json.dumps(ret), content_type='application/json')

def getByType(request):
    type = request.GET['type']
    
    Eps_type = Eps.objects.all().values('com_type').annotate(avg_001=Avg('pf_001'),avg_002=Avg('pf_002'),avg_003=Avg('pf_003'),avg_004=Avg('pf_004'),avg_011=Avg('pf_011'),avg_012=Avg('pf_012'),avg_013=Avg('pf_013'),avg_014=Avg('pf_014'),avg_021=Avg('pf_021'),avg_022=Avg('pf_022'),avg_023=Avg('pf_023'),avg_024=Avg('pf_024'),avg_031=Avg('pf_031'),avg_032=Avg('pf_032'),avg_033=Avg('pf_033'),avg_034=Avg('pf_034'),avg_041=Avg('pf_041'),avg_042=Avg('pf_042'),avg_043=Avg('pf_043'),avg_044=Avg('pf_044'),avg_051=Avg('pf_051'),avg_052=Avg('pf_052'),avg_053=Avg('pf_053'),avg_054=Avg('pf_054'),avg_061=Avg('pf_061'),avg_062=Avg('pf_062'),avg_063=Avg('pf_063'),avg_064=Avg('pf_064'),avg_071=Avg('pf_071'),avg_072=Avg('pf_072'),avg_073=Avg('pf_073'),avg_074=Avg('pf_074'),avg_081=Avg('pf_081'),avg_082=Avg('pf_082'),avg_083=Avg('pf_083'),avg_084=Avg('pf_084'),avg_091=Avg('pf_091'),avg_092=Avg('pf_092'),avg_093=Avg('pf_093'),avg_094=Avg('pf_094'),avg_101=Avg('pf_101'),avg_102=Avg('pf_102'),avg_103=Avg('pf_103'),avg_104=Avg('pf_104'),avg_111=Avg('pf_111'),avg_112=Avg('pf_112'),avg_113=Avg('pf_113'),avg_114=Avg('pf_114'),avg_121=Avg('pf_121'),avg_122=Avg('pf_122'),avg_123=Avg('pf_123'),avg_124=Avg('pf_124'),avg_131=Avg('pf_131'),avg_132=Avg('pf_132'),avg_133=Avg('pf_133'),avg_134=Avg('pf_134'),avg_141=Avg('pf_141'),avg_142=Avg('pf_142'),avg_143=Avg('pf_143'),avg_144=Avg('pf_144'),avg_151=Avg('pf_151'),avg_152=Avg('pf_152'),avg_153=Avg('pf_153'),avg_154=Avg('pf_154'),avg_161=Avg('pf_161'),avg_162=Avg('pf_162'),avg_163=Avg('pf_163'),avg_164=Avg('pf_164'),avg_171=Avg('pf_171'),avg_172=Avg('pf_172'),avg_173=Avg('pf_173'),avg_174=Avg('pf_174'),avg_181=Avg('pf_181'),avg_182=Avg('pf_182'),avg_183=Avg('pf_183')).values('com_type', 'avg_001','avg_002','avg_003','avg_004','avg_011','avg_012','avg_013','avg_014','avg_021','avg_022','avg_023','avg_024','avg_031','avg_032','avg_033','avg_034','avg_041','avg_042','avg_043','avg_044','avg_051','avg_052','avg_053','avg_054','avg_061','avg_062','avg_063','avg_064','avg_071','avg_072','avg_073','avg_074','avg_081','avg_082','avg_083','avg_084','avg_091','avg_092','avg_093','avg_094','avg_101','avg_102','avg_103','avg_104','avg_111','avg_112','avg_113','avg_114','avg_121','avg_122','avg_123','avg_124','avg_131','avg_132','avg_133','avg_134','avg_141','avg_142','avg_143','avg_144','avg_151','avg_152','avg_153','avg_154','avg_161','avg_162','avg_163','avg_164','avg_171','avg_172','avg_173','avg_174','avg_181','avg_182','avg_183')

    Jlr_type = Jlr.objects.all().values('com_type').annotate(avg_001=Avg('pf_001'),avg_002=Avg('pf_002'),avg_003=Avg('pf_003'),avg_004=Avg('pf_004'),avg_011=Avg('pf_011'),avg_012=Avg('pf_012'),avg_013=Avg('pf_013'),avg_014=Avg('pf_014'),avg_021=Avg('pf_021'),avg_022=Avg('pf_022'),avg_023=Avg('pf_023'),avg_024=Avg('pf_024'),avg_031=Avg('pf_031'),avg_032=Avg('pf_032'),avg_033=Avg('pf_033'),avg_034=Avg('pf_034'),avg_041=Avg('pf_041'),avg_042=Avg('pf_042'),avg_043=Avg('pf_043'),avg_044=Avg('pf_044'),avg_051=Avg('pf_051'),avg_052=Avg('pf_052'),avg_053=Avg('pf_053'),avg_054=Avg('pf_054'),avg_061=Avg('pf_061'),avg_062=Avg('pf_062'),avg_063=Avg('pf_063'),avg_064=Avg('pf_064'),avg_071=Avg('pf_071'),avg_072=Avg('pf_072'),avg_073=Avg('pf_073'),avg_074=Avg('pf_074'),avg_081=Avg('pf_081'),avg_082=Avg('pf_082'),avg_083=Avg('pf_083'),avg_084=Avg('pf_084'),avg_091=Avg('pf_091'),avg_092=Avg('pf_092'),avg_093=Avg('pf_093'),avg_094=Avg('pf_094'),avg_101=Avg('pf_101'),avg_102=Avg('pf_102'),avg_103=Avg('pf_103'),avg_104=Avg('pf_104'),avg_111=Avg('pf_111'),avg_112=Avg('pf_112'),avg_113=Avg('pf_113'),avg_114=Avg('pf_114'),avg_121=Avg('pf_121'),avg_122=Avg('pf_122'),avg_123=Avg('pf_123'),avg_124=Avg('pf_124'),avg_131=Avg('pf_131'),avg_132=Avg('pf_132'),avg_133=Avg('pf_133'),avg_134=Avg('pf_134'),avg_141=Avg('pf_141'),avg_142=Avg('pf_142'),avg_143=Avg('pf_143'),avg_144=Avg('pf_144'),avg_151=Avg('pf_151'),avg_152=Avg('pf_152'),avg_153=Avg('pf_153'),avg_154=Avg('pf_154'),avg_161=Avg('pf_161'),avg_162=Avg('pf_162'),avg_163=Avg('pf_163'),avg_164=Avg('pf_164'),avg_171=Avg('pf_171'),avg_172=Avg('pf_172'),avg_173=Avg('pf_173'),avg_174=Avg('pf_174'),avg_181=Avg('pf_181'),avg_182=Avg('pf_182'),avg_183=Avg('pf_183')).values('com_type', 'avg_001','avg_002','avg_003','avg_004','avg_011','avg_012','avg_013','avg_014','avg_021','avg_022','avg_023','avg_024','avg_031','avg_032','avg_033','avg_034','avg_041','avg_042','avg_043','avg_044','avg_051','avg_052','avg_053','avg_054','avg_061','avg_062','avg_063','avg_064','avg_071','avg_072','avg_073','avg_074','avg_081','avg_082','avg_083','avg_084','avg_091','avg_092','avg_093','avg_094','avg_101','avg_102','avg_103','avg_104','avg_111','avg_112','avg_113','avg_114','avg_121','avg_122','avg_123','avg_124','avg_131','avg_132','avg_133','avg_134','avg_141','avg_142','avg_143','avg_144','avg_151','avg_152','avg_153','avg_154','avg_161','avg_162','avg_163','avg_164','avg_171','avg_172','avg_173','avg_174','avg_181','avg_182','avg_183')

    Jsy_type = Jsy.objects.all().values('com_type').annotate(avg_001=Avg('pf_001'),avg_002=Avg('pf_002'),avg_003=Avg('pf_003'),avg_004=Avg('pf_004'),avg_011=Avg('pf_011'),avg_012=Avg('pf_012'),avg_013=Avg('pf_013'),avg_014=Avg('pf_014'),avg_021=Avg('pf_021'),avg_022=Avg('pf_022'),avg_023=Avg('pf_023'),avg_024=Avg('pf_024'),avg_031=Avg('pf_031'),avg_032=Avg('pf_032'),avg_033=Avg('pf_033'),avg_034=Avg('pf_034'),avg_041=Avg('pf_041'),avg_042=Avg('pf_042'),avg_043=Avg('pf_043'),avg_044=Avg('pf_044'),avg_051=Avg('pf_051'),avg_052=Avg('pf_052'),avg_053=Avg('pf_053'),avg_054=Avg('pf_054'),avg_061=Avg('pf_061'),avg_062=Avg('pf_062'),avg_063=Avg('pf_063'),avg_064=Avg('pf_064'),avg_071=Avg('pf_071'),avg_072=Avg('pf_072'),avg_073=Avg('pf_073'),avg_074=Avg('pf_074'),avg_081=Avg('pf_081'),avg_082=Avg('pf_082'),avg_083=Avg('pf_083'),avg_084=Avg('pf_084'),avg_091=Avg('pf_091'),avg_092=Avg('pf_092'),avg_093=Avg('pf_093'),avg_094=Avg('pf_094'),avg_101=Avg('pf_101'),avg_102=Avg('pf_102'),avg_103=Avg('pf_103'),avg_104=Avg('pf_104'),avg_111=Avg('pf_111'),avg_112=Avg('pf_112'),avg_113=Avg('pf_113'),avg_114=Avg('pf_114'),avg_121=Avg('pf_121'),avg_122=Avg('pf_122'),avg_123=Avg('pf_123'),avg_124=Avg('pf_124'),avg_131=Avg('pf_131'),avg_132=Avg('pf_132'),avg_133=Avg('pf_133'),avg_134=Avg('pf_134'),avg_141=Avg('pf_141'),avg_142=Avg('pf_142'),avg_143=Avg('pf_143'),avg_144=Avg('pf_144'),avg_151=Avg('pf_151'),avg_152=Avg('pf_152'),avg_153=Avg('pf_153'),avg_154=Avg('pf_154'),avg_161=Avg('pf_161'),avg_162=Avg('pf_162'),avg_163=Avg('pf_163'),avg_164=Avg('pf_164'),avg_171=Avg('pf_171'),avg_172=Avg('pf_172'),avg_173=Avg('pf_173'),avg_174=Avg('pf_174'),avg_181=Avg('pf_181'),avg_182=Avg('pf_182'),avg_183=Avg('pf_183')).values('com_type', 'avg_001','avg_002','avg_003','avg_004','avg_011','avg_012','avg_013','avg_014','avg_021','avg_022','avg_023','avg_024','avg_031','avg_032','avg_033','avg_034','avg_041','avg_042','avg_043','avg_044','avg_051','avg_052','avg_053','avg_054','avg_061','avg_062','avg_063','avg_064','avg_071','avg_072','avg_073','avg_074','avg_081','avg_082','avg_083','avg_084','avg_091','avg_092','avg_093','avg_094','avg_101','avg_102','avg_103','avg_104','avg_111','avg_112','avg_113','avg_114','avg_121','avg_122','avg_123','avg_124','avg_131','avg_132','avg_133','avg_134','avg_141','avg_142','avg_143','avg_144','avg_151','avg_152','avg_153','avg_154','avg_161','avg_162','avg_163','avg_164','avg_171','avg_172','avg_173','avg_174','avg_181','avg_182','avg_183')


    ret_eps = Eps_type.filter(com_type=type)[0]
    ret_jlr = Jlr_type.filter(com_type=type)[0]
    ret_jsy = Jsy_type.filter(com_type=type)[0]

    data = [[],[],[]]
    for i in range(0,19):
        for j in range(1,5):
            if i==18 and j==4: 
                break
            if i<10:
                index = 'avg_0'+str(i)+str(j)
                data[0].append(ret_eps[index])
                data[1].append(ret_jlr[index])
                data[2].append(ret_jsy[index])
            else:
                index = 'avg_'+str(i)+str(j)
                data[0].append(ret_eps[index])
                data[1].append(ret_jlr[index])
                data[2].append(ret_jsy[index])
    # print data
    change = [[],[],[]]
    for i in range(3):
        for j in range(len(data[i])-1):
            change[i].append(float('%.2f' %(data[i][j+1]-data[i][j])))

    changeToBar = [[[],[]],[[],[]],[[],[]]]
    for i in range(3):
        for j in range(len(change[i])):
            if change[i][j] >= 0:
                changeToBar[i][0].append(change[i][j])
                changeToBar[i][1].append('-')
            else:
                changeToBar[i][1].append(change[i][j])
                changeToBar[i][0].append('-')
    # print len(change[0])
    # print len(changeToBar[0][0])
    # print len(changeToBar[0][1])
    ret = {'data':data,'change':change,'changeToBar':changeToBar}
    return HttpResponse(json.dumps(ret), content_type='application/json')



def predictComView(request):
    context          = {}
    context['title'] = '公司'
    return render(request, 'predictCom.html', context)



def getByComName(request):
    name = request.GET.get('name')

    # print name

    Eps_com = Eps.objects.values('com_name', 'pf_001','pf_002','pf_003','pf_004','pf_011','pf_012','pf_013','pf_014','pf_021','pf_022','pf_023','pf_024','pf_031','pf_032','pf_033','pf_034','pf_041','pf_042','pf_043','pf_044','pf_051','pf_052','pf_053','pf_054','pf_061','pf_062','pf_063','pf_064','pf_071','pf_072','pf_073','pf_074','pf_081','pf_082','pf_083','pf_084','pf_091','pf_092','pf_093','pf_094','pf_101','pf_102','pf_103','pf_104','pf_111','pf_112','pf_113','pf_114','pf_121','pf_122','pf_123','pf_124','pf_131','pf_132','pf_133','pf_134','pf_141','pf_142','pf_143','pf_144','pf_151','pf_152','pf_153','pf_154','pf_161','pf_162','pf_163','pf_164','pf_171','pf_172','pf_173','pf_174','pf_181','pf_182','pf_183').filter(com_name = name)
    Jlr_com = Jlr.objects.values('com_name', 'pf_001','pf_002','pf_003','pf_004','pf_011','pf_012','pf_013','pf_014','pf_021','pf_022','pf_023','pf_024','pf_031','pf_032','pf_033','pf_034','pf_041','pf_042','pf_043','pf_044','pf_051','pf_052','pf_053','pf_054','pf_061','pf_062','pf_063','pf_064','pf_071','pf_072','pf_073','pf_074','pf_081','pf_082','pf_083','pf_084','pf_091','pf_092','pf_093','pf_094','pf_101','pf_102','pf_103','pf_104','pf_111','pf_112','pf_113','pf_114','pf_121','pf_122','pf_123','pf_124','pf_131','pf_132','pf_133','pf_134','pf_141','pf_142','pf_143','pf_144','pf_151','pf_152','pf_153','pf_154','pf_161','pf_162','pf_163','pf_164','pf_171','pf_172','pf_173','pf_174','pf_181','pf_182','pf_183').filter(com_name = name)
    # print Jlr_com
    Jsy_com = Jsy.objects.values('com_name', 'pf_001','pf_002','pf_003','pf_004','pf_011','pf_012','pf_013','pf_014','pf_021','pf_022','pf_023','pf_024','pf_031','pf_032','pf_033','pf_034','pf_041','pf_042','pf_043','pf_044','pf_051','pf_052','pf_053','pf_054','pf_061','pf_062','pf_063','pf_064','pf_071','pf_072','pf_073','pf_074','pf_081','pf_082','pf_083','pf_084','pf_091','pf_092','pf_093','pf_094','pf_101','pf_102','pf_103','pf_104','pf_111','pf_112','pf_113','pf_114','pf_121','pf_122','pf_123','pf_124','pf_131','pf_132','pf_133','pf_134','pf_141','pf_142','pf_143','pf_144','pf_151','pf_152','pf_153','pf_154','pf_161','pf_162','pf_163','pf_164','pf_171','pf_172','pf_173','pf_174','pf_181','pf_182','pf_183').filter(com_name = name)

    # if len(list(Eps_com)) == 0:

    
    ret_eps = list(Eps_com)[0]
    ret_jlr = list(Jlr_com)[0]
    ret_jsy = list(Jsy_com)[0]


    data = [[],[],[]]
    for i in range(0,19):
        for j in range(1,5):
            if i==18 and j==4: 
                break
            if i<10:
                index = 'pf_0'+str(i)+str(j)
                data[0].append(float(ret_eps[index]))
                data[1].append(float(ret_jlr[index]))
                data[2].append(float(ret_jsy[index]))
            else:
                index = 'pf_'+str(i)+str(j)
                data[0].append(float(ret_eps[index]))
                data[1].append(float(ret_jlr[index]))
                data[2].append(float(ret_jsy[index]))
    print data
    change = [[],[],[]]
    for i in range(3):
        for j in range(len(data[i])-1):
            change[i].append(float('%.2f' %(data[i][j+1]-data[i][j])))

    changeToBar = [[[],[]],[[],[]],[[],[]]]
    for i in range(3):
        for j in range(len(change[i])):
            if change[i][j] >= 0:
                changeToBar[i][0].append(change[i][j])
                changeToBar[i][1].append('-')
            else:
                changeToBar[i][1].append(change[i][j])
                changeToBar[i][0].append('-')
    # print len(change[0])
    # print len(changeToBar[0][0])
    # print len(changeToBar[0][1])

    radar = []
    for i in range(3):
        radar.append(data[i][-4:])
    print radar

    ret = {'data':data,'change':change,'changeToBar':changeToBar,'radar':radar}
    return HttpResponse(json.dumps(ret), content_type='application/json')


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


def charts(request):
    context          = {}
    return render(request, 'charts.html', context)