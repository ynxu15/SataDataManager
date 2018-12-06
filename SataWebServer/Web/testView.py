# -*- coding: utf-8 -*-

import time
from django.http import HttpResponse
 
#from TestModel.models import Test

from django.shortcuts import render_to_response

from Web.tasks import add
 
# 数据库操作
#def testdb(request):
#    test1 = Test(name='runoob')
#    test1.save()
#    add.delay(2,2)
#    return HttpResponse("<p>数据添加成功！</p>")

 
# 数据库操作
#def testdb1(request):
#    # 初始化
#    response = ""
#    response1 = ""
#    
#    
#    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
#    list = Test.objects.all()
#        
#    # filter相当于SQL中的WHERE，可设置条件过滤结果
#    response2 = Test.objects.filter(id=1) 
#    
#    # 获取单个对象
#    response3 = Test.objects.get(id=1) 
#    
#    # 限制返回的数据 相当于 SQL 中的 OFFSET 0 LIMIT 2;
#    Test.objects.order_by('name')[0:2]
#    
#    #数据排序
#    Test.objects.order_by("id")
#    
#    # 上面的方法可以连锁使用
#    Test.objects.filter(name="runoob").order_by("id")
#    
#    # 输出所有数据
#    for var in list:
#        response1 += var.name + " "
#    response = response1
#    return HttpResponse("<p>" + response + "</p>")


# 测试异步执行

def testCelery(request):
    return render_to_response('testCelery.html')

def testCeleryRe(request):
    #test1 = Test(name='runoob')
    #test1.save()
    n1 = 2
    n2 = 1
    res = add.delay(n1,n2)
    time.sleep(5)
    return HttpResponse("<p>%d + %d = %d</p>"%(n1, n2, res.get()))



# 表单
def search_form(request):
    return render_to_response('search_form.html')
 
# 接收请求数据
def search1(request):  
    request.encoding='utf-8'
    if 'q' in request.GET:
        message = '你搜索的内容为: ' + request.GET['q']
    else:
        message = '你提交了空表单'
    return HttpResponse(message)


from django.views.decorators import csrf
from django.shortcuts import render
# 接收POST请求数据
def search_post(request):
    ctx ={}
    if request.POST:
        if 'q' in request.POST:
            ctx['rlt'] = request.POST['q']
            return render(request, "post.html", ctx)
        if 'q1' in request.POST:
            ctx['rlt1'] = request.POST['q1']
            return render(request, "post.html", ctx)
    return render(request, "post.html", ctx)

#from django.views.decorators.csrf import csrf_exempt
import json
def terminal_svr(request):
    a = {}
    a["result"] = "post_success"
    return HttpResponse(json.dumps(a), content_type='application/json')


def svr(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'jsTest.html', context)


def addTest(request):
    return render(request, 'addTest.html')

def add1(request):
    a = request.GET['a']
    b = request.GET['b']
    a = int(a)
    b = int(b)
    return HttpResponse(str(a+b))


import json

def ajax_list(request):
    a = list(range(100))
    return HttpResponse(json.dumps(a), content_type='application/json')

def ajax_dict(request):
    name_dict = {'twz': 'Love python and Django', 'zqxt': 'I am teaching Django'}
    return HttpResponse(json.dumps(name_dict), content_type='application/json')


def myget(request):
    return render(request, 'myget.html')


