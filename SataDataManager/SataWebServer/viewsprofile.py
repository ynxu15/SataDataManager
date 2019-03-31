# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
import random


# Create your views here.


def index(request):
	return render(request, 'index.html')

def datatodic(): # to do
    return;

def randomsize(): # to do
    randomsize.index = randomsize.index+1
    print(randomsize.index)
    size = (randomsize.index < 10) and ((30-2*randomsize.index) + random.random() * 5) or (random.random() * 5)
    print(size)
    return str(size)
# WTH
def Persona_single(request):
	randomsize.index = 0
	a1=8.6
	a2=4.7
	a3=6.5
	evaluation_all=[[a1,a2,a3,0.5*a1+0.3*a2+0.3*a3]]
	data = {
		"dataCloud":[
            {"name": "谷歌","value": randomsize()},
            {"name": "Google","value": randomsize()},
            {"name": "搜索","value": randomsize()},
            {"name": "服务","value": randomsize()},
            {"name": "公司","value": randomsize()},
            {"name": "用户","value": randomsize()},
            {"name": "Android","value": randomsize()},
            {"name": "宣布","value": randomsize()},
            {"name": "Alphabet","value": randomsize()},
            {"name": "搜索引擎","value": randomsize()},
            {"name": "业务","value": randomsize()},
            {"name": "现任","value": randomsize()},
            {"name": "品牌","value": randomsize()},
            {"name": "网页","value": randomsize()},
            {"name": "提供","value": randomsize()},
            {"name": "美国","value": randomsize()},
            {"name": "开发","value": randomsize()},
            {"name": "Chrome","value": randomsize()},
            {"name": "全球","value": randomsize()},
            {"name": "操作系统","value": randomsize()},
            {"name": "浏览器","value": randomsize()},
            {"name": "拉里","value": randomsize()},
            {"name": "YouTube","value": randomsize()},
            {"name": "Gmail","value": randomsize()},
            {"name": "专利","value": randomsize()},
            {"name": "收购","value": randomsize()},
            {"name": "副总裁","value": randomsize()},
            {"name": "佩奇","value": randomsize()},
            {"name": "隐私","value": randomsize()},
            {"name": "软件","value": randomsize()},
            {"name": "FTC","value": randomsize()},
            {"name": "年度","value": randomsize()},
            {"name": "中国","value": randomsize()},
            {"name": "亿美元","value": randomsize()},
            {"name": "网站","value": randomsize()},
            {"name": "互联网","value": randomsize()},
            {"name": "发布","value": randomsize()},
            {"name": "推出","value": randomsize()},
            {"name": "正式","value": randomsize()},
            {"name": "BrandZ","value": randomsize()},
            {"name": "Glass","value": randomsize()},
            {"name": "Orkut","value": randomsize()},
            {"name": "页面","value": randomsize()},
            {"name": "购物","value": randomsize()},
            {"name": "艳照","value": randomsize()},
            {"name": "Web","value": randomsize()},
            {"name": "View","value": randomsize()},
            {"name": "总营收","value": randomsize()},
            {"name": "产品","value": randomsize()},
            {"name": "高级","value": randomsize()},
            {"name": "信息","value": randomsize()},
            {"name": "百强","value": randomsize()},
            {"name": "谢尔盖","value": randomsize()},
            {"name": "内容","value": randomsize()},
            {"name": "地图","value": randomsize()},
            {"name": "布林","value": randomsize()},
            {"name": "要求","value": randomsize()},
            {"name": "罚款","value": randomsize()},
            {"name": "运营","value": randomsize()},
            {"name": "功能","value": randomsize()},
            {"name": "最具","value": randomsize()},
            {"name": "首席","value": randomsize()},
            {"name": "技术","value": randomsize()},
            {"name": "数据中心","value": randomsize()},
            {"name": "第一","value": randomsize()},
            {"name": "广告","value": randomsize()},
            {"name": "事件","value": randomsize()},
            {"name": "反垄断","value": randomsize()},
            {"name": "欧盟","value": randomsize()},
            {"name": "编辑","value": randomsize()},
            {"name": "使用","value": randomsize()},
            {"name": "系统","value": randomsize()},
            {"name": "Brand","value": randomsize()},
            {"name": "AI","value": randomsize()},
            {"name": "PageRank","value": randomsize()},
            {"name": "Linux","value": randomsize()},
            {"name": "Nexus","value": randomsize()},
            {"name": "Play","value": randomsize()},
            {"name": "OS","value": randomsize()},
            {"name": "Video","value": randomsize()},
            {"name": "Blogger","value": randomsize()},
            {"name": "Picasa","value": randomsize()},
            {"name": "USA","value": randomsize()},
            {"name": "Safari","value": randomsize()},
            {"name": "埃里克","value": randomsize()},
            {"name": "删除","value": randomsize()},
            {"name": "应用","value": randomsize()},
            {"name": "架构","value": randomsize()},
            {"name": "工程部","value": randomsize()},
            {"name": "万美元","value": randomsize()},
            {"name": "开发者","value": randomsize()},
            {"name": "关闭","value": randomsize()},
            {"name": "网络","value": randomsize()},
            {"name": "访问","value": randomsize()},
            {"name": "市场","value": randomsize()},
            {"name": "免费","value": randomsize()},
            {"name": "成为","value": randomsize()},
            {"name": "亚马逊","value": randomsize()},
            {"name": "包括","value": randomsize()},
            {"name": "施密特","value": randomsize()},
            {"name": "董事","value": randomsize()},
            {"name": "罚单","value": randomsize()},
            {"name": "成立","value": randomsize()},
            {"name": "中文","value": randomsize()},
            {"name": "电子邮件","value": randomsize()},
            {"name": "世界","value": randomsize()},
            {"name": "无人机","value": randomsize()},
            {"name": "一款","value": randomsize()},
            {"name": "数据","value": randomsize()},
            {"name": "企业","value": randomsize()},
            {"name": "实验室","value": randomsize()},
            {"name": "苹果","value": randomsize()},
            {"name": "巨头","value": randomsize()},
            {"name": "管理","value": randomsize()},
            {"name": "违反","value": randomsize()},
            {"name": "欧元","value": randomsize()},
            {"name": "旗下","value": randomsize()},
            {"name": "一个","value": randomsize()},
            {"name": "创始人","value": randomsize()},
            {"name": "浏览","value": randomsize()},
            {"name": "名为","value": randomsize()},
            {"name": "Finance","value": randomsize()},
            {"name": "皮查","value": randomsize()},
            {"name": "安卓","value": randomsize()},
            {"name": "Project","value": randomsize()},
            {"name": "Book","value": randomsize()},
            {"name": "Search","value": randomsize()},
            {"name": "Answers","value": randomsize()},
            {"name": "Local","value": randomsize()},
            {"name": "iGoogle","value": randomsize()},
            {"name": "SketchUp","value": randomsize()},
            {"name": "Amphitheatre","value": randomsize()},
            {"name": "Parkway","value": randomsize()},
            {"name": "Mountain","value": randomsize()},
            {"name": "CA","value": randomsize()},
            {"name": "创建","value": randomsize()},
            {"name": "主要","value": randomsize()},
            {"name": "获得","value": randomsize()},
            {"name": "价值","value": randomsize()},
            {"name": "和解","value": randomsize()},
            {"name": "获奖","value": randomsize()},
            {"name": "专利申请","value": randomsize()},
            {"name": "移动","value": randomsize()},
            {"name": "领域","value": randomsize()},
            {"name": "开源","value": randomsize()},
            {"name": "视频","value": randomsize()},
            {"name": "注册商标","value": randomsize()},
            {"name": "在线","value": randomsize()},
            {"name": "眼镜","value": randomsize()},
            {"name": "部门","value": randomsize()},
            {"name": "手机","value": randomsize()},
            {"name": "大会","value": randomsize()},
            {"name": "智能手机","value": randomsize()},
            {"name": "工具","value": randomsize()},
            {"name": "申请","value": randomsize()},
            {"name": "翻译","value": randomsize()},
            {"name": "首款","value": randomsize()},
            {"name": "工作","value": randomsize()},
            {"name": "资料","value": randomsize()},
            {"name": "目录","value": randomsize()},
            {"name": "科技","value": randomsize()},
            {"name": "总裁","value": randomsize()},
            {"name": "相关","value": randomsize()},
            {"name": "管理层","value": randomsize()},
            {"name": "卫星","value": randomsize()},
            {"name": "盈利","value": randomsize()},
            {"name": "罚金","value": randomsize()},
            {"name": "人工智能","value": randomsize()},
            {"name": "联合","value": randomsize()},
            {"name": "总部","value": randomsize()},
            {"name": "荷兰","value": randomsize()},
            {"name": "桌面","value": randomsize()},
            {"name": "拉蒙德","value": randomsize()},
            {"name": "安全","value": randomsize()},
            {"name": "合作","value": randomsize()},
            {"name": "标识","value": randomsize()},
            {"name": "表示","value": randomsize()},
            {"name": "已经","value": randomsize()},
            {"name": "研发","value": randomsize()},
            {"name": "屏蔽","value": randomsize()},
            {"name": "微软","value": randomsize()},
            {"name": "个性化","value": randomsize()},
            {"name": "男子","value": randomsize()},
            {"name": "最大","value": randomsize()},
            {"name": "关键词","value": randomsize()},
            {"name": "榜单","value": randomsize()},
            {"name": "整合","value": randomsize()},
            {"name": "部分","value": randomsize()},
            {"name": "数据保护","value": randomsize()},
            {"name": "本年度","value": randomsize()},
            {"name": "办公室","value": randomsize()},
            {"name": "自动","value": randomsize()},
            {"name": "汽车","value": randomsize()},
            {"name": "处以","value": randomsize()},
            {"name": "名称","value": randomsize()},
            {"name": "允许","value": randomsize()},
            {"name": "追踪","value": randomsize()},
            {"name": "手机操作系统","value": randomsize()},
            {"name": "执行官","value": randomsize()},
            {"name": "设置","value": randomsize()},
            {"name": "支持","value": randomsize()},
            {"name": "公布","value": randomsize()},
            {"name": "硬件","value": randomsize()},
            {"name": "虚拟","value": randomsize()},
            {"name": "地球","value": randomsize()},
            {"name": "科什","value": randomsize()},
            {"name": "环境保护局","value": randomsize()},

],

# 重复传送
        "graphdata":[
            {

                "name":"综合评分"+str(evaluation_all[0][3]),# name不能出现数字
                #"name":"综合评分",
                "symbolSize":120,
                "category":0,
                "draggable":"true"
            },
            {

                "name":"发展能力"+str(evaluation_all[0][0]),
                #"name":"发展能力",
                "symbolSize":90,
                "category":1,
                "draggable":"true"
            },
            {

                "name":"创新潜力"+str(evaluation_all[0][1]),
                #"name":"创新潜力",
                "symbolSize":90,
                "category":1,
                "draggable":"true"
            },
            {

                "name":"风险评估"+str(evaluation_all[0][2]),
                #"name":"风险评估",
                "symbolSize":90,
                "category":1,
                "draggable":"true"
            },
#            {
#
#                "name":"专利/论文数",
#                "symbolSize":40,
#                "category":2,
#                "draggable":"true"
#            },
#            {
#                "name":"营业总收入",
#                "symbolSize":40,
#                "category":2,
#                "draggable":"true"
#            },
#            {
#                "name":"总负债",
#                "symbolSize":40,
#                "category":2,
#                "draggable":"true"
#            },
        ],

        "graphlinks":[

            {
                "source":"发展能力",
                "target":"综合评分",
                "value": 100,
            },

            {
                "source":"创新潜力",
                "target":"综合评分",
                "lineStyle":{
                    "normal":{
                        "color":"source"
                    }
                }
            },

            {
                "source":"风险评估",
                "target":"综合评分",
                "lineStyle":{
                    "normal":{
                        "color":"source"
                    }
                }
            },

            {
                "source":"专利/论文数",
                "target":"创新潜力",
                "lineStyle":{
                    "normal":{
                        "color":"source"
                    }
                }
            },
            {
                "source":"营业总收入",
                "target":"发展能力",
                "lineStyle":{
                    "normal":{
                        "color":"source"
                    }
                }
            },
            {
                "source":"总负债",
                "target":"风险评估",
                "lineStyle":{
                    "normal":{
                        "color":"source"
                    }
                }
            },
        ],
	}
	#print(data['dataCloud'])
	return render(request, 'Persona_single.html', {'data':json.dumps(data)})
	
def Persona(request):
    	randomsize.index = 0
    	a1=8.6
    	a2=4.7
    	a3=6.5
    	evaluation_all=[[a1,a2,a3,0.5*a1+0.3*a2+0.3*a3]]
    	data = {
    		"dataCloud":[
                {"name": "谷歌","value": randomsize()},
                {"name": "Google","value": randomsize()},
                {"name": "搜索","value": randomsize()},
                {"name": "服务","value": randomsize()},
                {"name": "公司","value": randomsize()},
                {"name": "用户","value": randomsize()},
                {"name": "Android","value": randomsize()},
                {"name": "宣布","value": randomsize()},
                {"name": "Alphabet","value": randomsize()},
                {"name": "搜索引擎","value": randomsize()},
                {"name": "业务","value": randomsize()},
                {"name": "现任","value": randomsize()},
                {"name": "品牌","value": randomsize()},
                {"name": "网页","value": randomsize()},
                {"name": "提供","value": randomsize()},
                {"name": "美国","value": randomsize()},
                {"name": "开发","value": randomsize()},
                {"name": "Chrome","value": randomsize()},
                {"name": "全球","value": randomsize()},
                {"name": "操作系统","value": randomsize()},
                {"name": "浏览器","value": randomsize()},
                {"name": "拉里","value": randomsize()},
                {"name": "YouTube","value": randomsize()},
                {"name": "Gmail","value": randomsize()},
                {"name": "专利","value": randomsize()},
                {"name": "收购","value": randomsize()},
                {"name": "副总裁","value": randomsize()},
                {"name": "佩奇","value": randomsize()},
                {"name": "隐私","value": randomsize()},
                {"name": "软件","value": randomsize()},
                {"name": "FTC","value": randomsize()},
                {"name": "年度","value": randomsize()},
                {"name": "中国","value": randomsize()},
                {"name": "亿美元","value": randomsize()},
                {"name": "网站","value": randomsize()},
                {"name": "互联网","value": randomsize()},
                {"name": "发布","value": randomsize()},
                {"name": "推出","value": randomsize()},
                {"name": "正式","value": randomsize()},
                {"name": "BrandZ","value": randomsize()},
                {"name": "Glass","value": randomsize()},
                {"name": "Orkut","value": randomsize()},
                {"name": "页面","value": randomsize()},
                {"name": "购物","value": randomsize()},
                {"name": "艳照","value": randomsize()},
                {"name": "Web","value": randomsize()},
                {"name": "View","value": randomsize()},
                {"name": "总营收","value": randomsize()},
                {"name": "产品","value": randomsize()},
                {"name": "高级","value": randomsize()},
                {"name": "信息","value": randomsize()},
                {"name": "百强","value": randomsize()},
                {"name": "谢尔盖","value": randomsize()},
                {"name": "内容","value": randomsize()},
                {"name": "地图","value": randomsize()},
                {"name": "布林","value": randomsize()},
                {"name": "要求","value": randomsize()},
                {"name": "罚款","value": randomsize()},
                {"name": "运营","value": randomsize()},
                {"name": "功能","value": randomsize()},
                {"name": "最具","value": randomsize()},
                {"name": "首席","value": randomsize()},
                {"name": "技术","value": randomsize()},
                {"name": "数据中心","value": randomsize()},
                {"name": "第一","value": randomsize()},
                {"name": "广告","value": randomsize()},
                {"name": "事件","value": randomsize()},
                {"name": "反垄断","value": randomsize()},
                {"name": "欧盟","value": randomsize()},
                {"name": "编辑","value": randomsize()},
                {"name": "使用","value": randomsize()},
                {"name": "系统","value": randomsize()},
                {"name": "Brand","value": randomsize()},
                {"name": "AI","value": randomsize()},
                {"name": "PageRank","value": randomsize()},
                {"name": "Linux","value": randomsize()},
                {"name": "Nexus","value": randomsize()},
                {"name": "Play","value": randomsize()},
                {"name": "OS","value": randomsize()},
                {"name": "Video","value": randomsize()},
                {"name": "Blogger","value": randomsize()},
                {"name": "Picasa","value": randomsize()},
                {"name": "USA","value": randomsize()},
                {"name": "Safari","value": randomsize()},
                {"name": "埃里克","value": randomsize()},
                {"name": "删除","value": randomsize()},
                {"name": "应用","value": randomsize()},
                {"name": "架构","value": randomsize()},
                {"name": "工程部","value": randomsize()},
                {"name": "万美元","value": randomsize()},
                {"name": "开发者","value": randomsize()},
                {"name": "关闭","value": randomsize()},
                {"name": "网络","value": randomsize()},
                {"name": "访问","value": randomsize()},
                {"name": "市场","value": randomsize()},
                {"name": "免费","value": randomsize()},
                {"name": "成为","value": randomsize()},
                {"name": "亚马逊","value": randomsize()},
                {"name": "包括","value": randomsize()},
                {"name": "施密特","value": randomsize()},
                {"name": "董事","value": randomsize()},
                {"name": "罚单","value": randomsize()},
                {"name": "成立","value": randomsize()},
                {"name": "中文","value": randomsize()},
                {"name": "电子邮件","value": randomsize()},
                {"name": "世界","value": randomsize()},
                {"name": "无人机","value": randomsize()},
                {"name": "一款","value": randomsize()},
                {"name": "数据","value": randomsize()},
                {"name": "企业","value": randomsize()},
                {"name": "实验室","value": randomsize()},
                {"name": "苹果","value": randomsize()},
                {"name": "巨头","value": randomsize()},
                {"name": "管理","value": randomsize()},
                {"name": "违反","value": randomsize()},
                {"name": "欧元","value": randomsize()},
                {"name": "旗下","value": randomsize()},
                {"name": "一个","value": randomsize()},
                {"name": "创始人","value": randomsize()},
                {"name": "浏览","value": randomsize()},
                {"name": "名为","value": randomsize()},
                {"name": "Finance","value": randomsize()},
                {"name": "皮查","value": randomsize()},
                {"name": "安卓","value": randomsize()},
                {"name": "Project","value": randomsize()},
                {"name": "Book","value": randomsize()},
                {"name": "Search","value": randomsize()},
                {"name": "Answers","value": randomsize()},
                {"name": "Local","value": randomsize()},
                {"name": "iGoogle","value": randomsize()},
                {"name": "SketchUp","value": randomsize()},
                {"name": "Amphitheatre","value": randomsize()},
                {"name": "Parkway","value": randomsize()},
                {"name": "Mountain","value": randomsize()},
                {"name": "CA","value": randomsize()},
                {"name": "创建","value": randomsize()},
                {"name": "主要","value": randomsize()},
                {"name": "获得","value": randomsize()},
                {"name": "价值","value": randomsize()},
                {"name": "和解","value": randomsize()},
                {"name": "获奖","value": randomsize()},
                {"name": "专利申请","value": randomsize()},
                {"name": "移动","value": randomsize()},
                {"name": "领域","value": randomsize()},
                {"name": "开源","value": randomsize()},
                {"name": "视频","value": randomsize()},
                {"name": "注册商标","value": randomsize()},
                {"name": "在线","value": randomsize()},
                {"name": "眼镜","value": randomsize()},
                {"name": "部门","value": randomsize()},
                {"name": "手机","value": randomsize()},
                {"name": "大会","value": randomsize()},
                {"name": "智能手机","value": randomsize()},
                {"name": "工具","value": randomsize()},
                {"name": "申请","value": randomsize()},
                {"name": "翻译","value": randomsize()},
                {"name": "首款","value": randomsize()},
                {"name": "工作","value": randomsize()},
                {"name": "资料","value": randomsize()},
                {"name": "目录","value": randomsize()},
                {"name": "科技","value": randomsize()},
                {"name": "总裁","value": randomsize()},
                {"name": "相关","value": randomsize()},
                {"name": "管理层","value": randomsize()},
                {"name": "卫星","value": randomsize()},
                {"name": "盈利","value": randomsize()},
                {"name": "罚金","value": randomsize()},
                {"name": "人工智能","value": randomsize()},
                {"name": "联合","value": randomsize()},
                {"name": "总部","value": randomsize()},
                {"name": "荷兰","value": randomsize()},
                {"name": "桌面","value": randomsize()},
                {"name": "拉蒙德","value": randomsize()},
                {"name": "安全","value": randomsize()},
                {"name": "合作","value": randomsize()},
                {"name": "标识","value": randomsize()},
                {"name": "表示","value": randomsize()},
                {"name": "已经","value": randomsize()},
                {"name": "研发","value": randomsize()},
                {"name": "屏蔽","value": randomsize()},
                {"name": "微软","value": randomsize()},
                {"name": "个性化","value": randomsize()},
                {"name": "男子","value": randomsize()},
                {"name": "最大","value": randomsize()},
                {"name": "关键词","value": randomsize()},
                {"name": "榜单","value": randomsize()},
                {"name": "整合","value": randomsize()},
                {"name": "部分","value": randomsize()},
                {"name": "数据保护","value": randomsize()},
                {"name": "本年度","value": randomsize()},
                {"name": "办公室","value": randomsize()},
                {"name": "自动","value": randomsize()},
                {"name": "汽车","value": randomsize()},
                {"name": "处以","value": randomsize()},
                {"name": "名称","value": randomsize()},
                {"name": "允许","value": randomsize()},
                {"name": "追踪","value": randomsize()},
                {"name": "手机操作系统","value": randomsize()},
                {"name": "执行官","value": randomsize()},
                {"name": "设置","value": randomsize()},
                {"name": "支持","value": randomsize()},
                {"name": "公布","value": randomsize()},
                {"name": "硬件","value": randomsize()},
                {"name": "虚拟","value": randomsize()},
                {"name": "地球","value": randomsize()},
                {"name": "科什","value": randomsize()},
                {"name": "环境保护局","value": randomsize()},

    ],

    # 重复传送
            "graphdata":[
                {

                    "name":"综合评分"+str(evaluation_all[0][3]),# name不能出现数字
                    #"name":"综合评分",
                    "symbolSize":120,
                    "category":0,
                    "draggable":"true"
                },
                {

                    "name":"发展能力"+str(evaluation_all[0][0]),
                    #"name":"发展能力",
                    "symbolSize":90,
                    "category":1,
                    "draggable":"true"
                },
                {

                    "name":"创新潜力"+str(evaluation_all[0][1]),
                    #"name":"创新潜力",
                    "symbolSize":90,
                    "category":1,
                    "draggable":"true"
                },
                {

                    "name":"风险评估"+str(evaluation_all[0][2]),
                    #"name":"风险评估",
                    "symbolSize":90,
                    "category":1,
                    "draggable":"true"
                },
    #            {
    #
    #                "name":"专利/论文数",
    #                "symbolSize":40,
    #                "category":2,
    #                "draggable":"true"
    #            },
    #            {
    #                "name":"营业总收入",
    #                "symbolSize":40,
    #                "category":2,
    #                "draggable":"true"
    #            },
    #            {
    #                "name":"总负债",
    #                "symbolSize":40,
    #                "category":2,
    #                "draggable":"true"
    #            },
            ],

            "graphlinks":[

                {
                    "source":"发展能力",
                    "target":"综合评分",
                    "value": 100,
                },

                {
                    "source":"创新潜力",
                    "target":"综合评分",
                    "lineStyle":{
                        "normal":{
                            "color":"source"
                        }
                    }
                },

                {
                    "source":"风险评估",
                    "target":"综合评分",
                    "lineStyle":{
                        "normal":{
                            "color":"source"
                        }
                    }
                },

                {
                    "source":"专利/论文数",
                    "target":"创新潜力",
                    "lineStyle":{
                        "normal":{
                            "color":"source"
                        }
                    }
                },
                {
                    "source":"营业总收入",
                    "target":"发展能力",
                    "lineStyle":{
                        "normal":{
                            "color":"source"
                        }
                    }
                },
                {
                    "source":"总负债",
                    "target":"风险评估",
                    "lineStyle":{
                        "normal":{
                            "color":"source"
                        }
                    }
                },
            ],
    	}
    	#print(data['dataCloud'])
    	return render(request, 'Persona.html', {'data':json.dumps(data)})
		
def org(request):
	return render(request, 'org.html')











def back_page(request):
	return render(request, 'back.html')

def login(request):
	return render(request, 'login.html')

def tst(request):
	List = ['自强学堂', '渲染Json到模板']
	Dict = {'site': '自强学堂', 'author': '涂伟忠'}
	return render(request, 'tst.html', {
            'List': json.dumps(List),
            'Dict': json.dumps(Dict)
        })
        
def myget(request):
	return render(request, 'myget.html')

def add(request):
	#print 'i am in add'
	a = request.GET['a']
	b = request.GET['b']
	a = int(a)
	b = int(b)
	return HttpResponse(str(a+b))

def test(request):
	return render(request, 'test.html')
	
@csrf_exempt #增加装饰器，作用是跳过 csrf 中间件的保护
def cal(request):
	print(request.POST)
	n1 = int(request.POST.get('n1'))
	n2 = int(request.POST.get('n2'))
	ret = n1+n2
	return HttpResponse(ret)

