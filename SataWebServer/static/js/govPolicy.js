


function setChart1(){
	// 基于准备好的dom，初始化echarts实例
     var myChart = echarts.init(document.getElementById('chart1'));

        // 指定图表的配置项和数据
       app.title = '堆叠柱状图';

	option = {
		tooltip : {
			trigger: 'axis',
			axisPointer : {            // 坐标轴指示器，坐标轴触发有效
				type : 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
			}
		},
		legend: {
			data:['直接访问','邮件营销','联盟广告','视频广告','搜索引擎','百度','谷歌','必应','其他']
		},
		grid: {
			left: '3%',
			right: '4%',
			bottom: '3%',
			containLabel: true
		},
		xAxis : [
			{
				type : 'category',
				data : ['周一','周二','周三','周四','周五','周六','周日']
			}
		],
		yAxis : [
			{
				type : 'value'
			}
		],
		series : [
			{
				name:'直接访问',
				type:'bar',
				data:[320, 332, 301, 334, 390, 330, 320]
			},
			{
				name:'邮件营销',
				type:'bar',
				stack: '广告',
				data:[120, 132, 101, 134, 90, 230, 210]
			},
			{
				name:'联盟广告',
				type:'bar',
				stack: '广告',
				data:[220, 182, 191, 234, 290, 330, 310]
			},
			{
				name:'视频广告',
				type:'bar',
				stack: '广告',
				data:[150, 232, 201, 154, 190, 330, 410]
			},
			{
				name:'搜索引擎',
				type:'bar',
				data:[862, 1018, 964, 1026, 1679, 1600, 1570],
				markLine : {
					lineStyle: {
						normal: {
							type: 'dashed'
						}
					},
					data : [
						[{type : 'min'}, {type : 'max'}]
					]
				}
			},
			{
				name:'百度',
				type:'bar',
				barWidth : 5,
				stack: '搜索引擎',
				data:[620, 732, 701, 734, 1090, 1130, 1120]
			},
			{
				name:'谷歌',
				type:'bar',
				stack: '搜索引擎',
				data:[120, 132, 101, 134, 290, 230, 220]
			},
			{
				name:'必应',
				type:'bar',
				stack: '搜索引擎',
				data:[60, 72, 71, 74, 190, 130, 110]
			},
			{
				name:'其他',
				type:'bar',
				stack: '搜索引擎',
				data:[62, 82, 91, 84, 109, 110, 120]
			}
		]
	};
        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option);
}

function setChart2(){
	// 基于准备好的dom，初始化echarts实例
     //var myChart = echarts.init(document.getElementById('chart2'));

        // 指定图表的配置项和数据
  
var myChart = echarts.init(document.getElementById('chart2'));
	var option = {
		title: {
			text : '上海地图',
			subtext : '-。-'
		},
		tooltip : {
			trigger: 'item',
			formatter: function(a){
				return a[2];
			}
		},
		legend: {
			orient: 'vertical',
			x:'right',
			data:['数据名称']
		},
		dataRange: {
			min: 0,
			max: 1000,
			color:['orange','yellow'],
			text:['高','低'],           // 文本，默认为数值文本
			calculable : true
		},
		series : [
			{
				name: '数据名称',
				type: 'map',
				mapType: '上海',
				selectedMode : 'single',
				itemStyle:{
					normal:{label:{show:true}},
					emphasis:{label:{show:true}}
				},
				data:[
					{name: '崇明县',value: Math.round(Math.random()*1000)},
					{name: '宝山区',value: Math.round(Math.random()*1000)},
					{name: '嘉定区',value: Math.round(Math.random()*1000)},
					{name: '青浦区',value: Math.round(Math.random()*1000)},
					{name: '杨浦区',value: Math.round(Math.random()*1000)},
					{name: '虹口区',value: Math.round(Math.random()*1000)},
					{name: '闸北区',value: Math.round(Math.random()*1000)},
					{name: '普陀区',value: Math.round(Math.random()*1000)},
					{name: '静安区',value: Math.round(Math.random()*1000)},
					{name: '黄浦区',value: Math.round(Math.random()*1000)},
					{name: '卢湾区',value: Math.round(Math.random()*1000)},
					{name: '长宁区',value: Math.round(Math.random()*1000)},
					{name: '徐汇区',value: Math.round(Math.random()*1000)},
					{name: '浦东新区',value: Math.round(Math.random()*1000)},
					{name: '松江区',value: Math.round(Math.random()*1000)},
					{name: '闵行区',value: Math.round(Math.random()*1000)},
					{name: '金山区',value: Math.round(Math.random()*1000)},
					{name: '奉贤区',value: Math.round(Math.random()*1000)},
					{name: '南汇区',value: Math.round(Math.random()*1000)}
				]
			}
		]
	};
	myChart.setOption(option);          
        // 使用刚指定的配置项和数据显示图表。
        //myChart.setOption(option);
}

function setChart3(){
	// 基于准备好的dom，初始化echarts实例
     var myChart = echarts.init(document.getElementById('chart3'));

        // 指定图表的配置项和数据
       app.title = '堆叠柱状图';

option = {
    tooltip : {
        trigger: 'axis',
        axisPointer : {            // 坐标轴指示器，坐标轴触发有效
            type : 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
        }
    },
    legend: {
        data:['直接访问','邮件营销','联盟广告','视频广告','搜索引擎','百度','谷歌','必应','其他']
    },
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },
    xAxis : [
        {
            type : 'category',
            data : ['周一','周二','周三','周四','周五','周六','周日']
        }
    ],
    yAxis : [
        {
            type : 'value'
        }
    ],
    series : [
        {
            name:'直接访问',
            type:'bar',
            data:[320, 332, 301, 334, 390, 330, 320]
        },
        {
            name:'邮件营销',
            type:'bar',
            stack: '广告',
            data:[120, 132, 101, 134, 90, 230, 210]
        },
        {
            name:'联盟广告',
            type:'bar',
            stack: '广告',
            data:[220, 182, 191, 234, 290, 330, 310]
        },
        {
            name:'视频广告',
            type:'bar',
            stack: '广告',
            data:[150, 232, 201, 154, 190, 330, 410]
        },
        {
            name:'搜索引擎',
            type:'bar',
            data:[862, 1018, 964, 1026, 1679, 1600, 1570],
            markLine : {
                lineStyle: {
                    normal: {
                        type: 'dashed'
                    }
                },
                data : [
                    [{type : 'min'}, {type : 'max'}]
                ]
            }
        },
        {
            name:'百度',
            type:'bar',
            barWidth : 5,
            stack: '搜索引擎',
            data:[620, 732, 701, 734, 1090, 1130, 1120]
        },
        {
            name:'谷歌',
            type:'bar',
            stack: '搜索引擎',
            data:[120, 132, 101, 134, 290, 230, 220]
        },
        {
            name:'必应',
            type:'bar',
            stack: '搜索引擎',
            data:[60, 72, 71, 74, 190, 130, 110]
        },
        {
            name:'其他',
            type:'bar',
            stack: '搜索引擎',
            data:[62, 82, 91, 84, 109, 110, 120]
        }
    ]
};

        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option);
}

          
function setChart4(){
	// 基于准备好的dom，初始化echarts实例
     var myChart = echarts.init(document.getElementById('chart4'));

        // 指定图表的配置项和数据
       var option = {
           barWidth:30,//条形的宽的为30
           tooltip: {},
           legend: {//说明
                    //orient: 'vertical', //说明显示在的位置所在
                    // center: 'center ',//说明的位置居中显示 默认居中横排显示
                    data:['累积', '新增']//数据说明
                    },
           xAxis: {//X轴上的内容
                    type : 'category',
                    axisLabel:{
                        //横坐标上的文字斜着显示 文字颜色 begin 
                             interval:0,
                            rotate:45,
                             margin:2,
                             textStyle:{color:"#ec6869" }
                        //横坐标上的文字换行显示 文字颜色end
                             },
                    type : 'category',
                    data: ["饭店供应商数量","酒店供应商数量","合作大巴公司数量","保险供应商数量","票务供应商数量"]
                  },
            yAxis: {//Y轴上的内容
                     type : 'value'
                   },
            series: [
                //第一条数据 begin
                    {
                    type: 'bar',//Echart 柱状图（bar）
                    name:'累积',
                    data: [610, 700, 400, 600, 500],
                        //柱状条颜色的设置为#eb6768 begin
                        itemStyle: {
                                normal: {
                                color: '#eb6768',
                                shadowBlur: 2,
                                shadowColor: 'rgba(3, 3, 4, 0.5)'
                                        }
                                    }
                        //柱状条颜色的设置为#eb6768 end
                    },
                 //第一条数据 end
                 
                 //第二条数据 begin    
                    {
                    type: 'bar',
                    name:'新增',
                    data: [510, 400, 300, 200, 100],
                    //柱状条颜色的设置为#eb6768 begin
                    itemStyle: {
                            normal: {
                                color: '#3b8ede',
                                shadowBlur: 2,
                                shadowColor: 'rgba(3, 3, 4, 0.5)'
                                  }
                               }
                    //柱状条颜色的设置为#eb6768  end    
                  } 
               //第二条数据 end    
               ] 
             };
       

        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option);
}

function setChart5(){
	// 基于准备好的dom，初始化echarts实例
     var myChart = echarts.init(document.getElementById('chart5'));

        // 指定图表的配置项和数据
var labelRight = {
    normal: {
        position: 'right'
    }
};
option = {
    //title: {
    //    text: '交错正负轴标签',
    //},
    tooltip : {
        trigger: 'axis',
        axisPointer : {            // 坐标轴指示器，坐标轴触发有效
            type : 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
        }
    },
    grid: {
        top: 80,
        bottom: 30
    },
    xAxis: {
        type : 'value',
        position: 'top',
        splitLine: {lineStyle:{type:'dashed'}},
    },
    yAxis: {
        type : 'category',
        axisLine: {show: false},
        axisLabel: {show: false},
        axisTick: {show: false},
        splitLine: {show: false},
        data : ['ten', 'nine', 'eight', 'seven', 'six', 'five', 'four', 'three', 'two', 'one']
    },
    series : [
        {
            name:'生活费',
            type:'bar',
            stack: '总量',
            label: {
                normal: {
                    show: true,
                    formatter: '{b}'
                }
            },
            data:[
                {value: -0.07, label: labelRight},
                {value: -0.09, label: labelRight},
                0.2, 0.44,
                {value: -0.23, label: labelRight},
                0.08,
                {value: -0.17, label: labelRight},
                0.47,
                {value: -0.36, label: labelRight},
                0.18
            ]
        }
    ]
};


        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option);
}

function setChart6(){
	// 基于准备好的dom，初始化echarts实例
     var myChart = echarts.init(document.getElementById('chart6'));

        // 指定图表的配置项和数据

var weatherIcons = {
    'Sunny': './data/asset/img/weather/sunny_128.png',
    'Cloudy': './data/asset/img/weather/cloudy_128.png',
    'Showers': './data/asset/img/weather/showers_128.png'
};

var seriesLabel = {
    normal: {
        show: true,
        textBorderColor: '#333',
        textBorderWidth: 2
    }
}

option = {
    title: {
        text: 'Wheater Statistics'
    },
    tooltip: {
        trigger: 'axis',
        axisPointer: {
            type: 'shadow'
        }
    },
    legend: {
        data: ['City Alpha', 'City Beta', 'City Gamma']
    },
    grid: {
        left: 100
    },
    toolbox: {
        show: true,
        feature: {
            saveAsImage: {}
        }
    },
    xAxis: {
        type: 'value',
        name: 'Days',
        axisLabel: {
            formatter: '{value}'
        }
    },
    yAxis: {
        type: 'category',
        inverse: true,
        data: ['Sunny', 'Cloudy', 'Showers'],
        axisLabel: {
            formatter: function (value) {
                return '{' + value + '| }\n{value|' + value + '}';
            },
            margin: 20,
            rich: {
                value: {
                    lineHeight: 30,
                    align: 'center'
                },
                Sunny: {
                    height: 40,
                    align: 'center',
                    backgroundColor: {
                        image: weatherIcons.Sunny
                    }
                },
                Cloudy: {
                    height: 40,
                    align: 'center',
                    backgroundColor: {
                        image: weatherIcons.Cloudy
                    }
                },
                Showers: {
                    height: 40,
                    align: 'center',
                    backgroundColor: {
                        image: weatherIcons.Showers
                    }
                }
            }
        }
    },
    series: [
        {
            name: 'City Alpha',
            type: 'bar',
            data: [165, 170, 30],
            label: seriesLabel,
            markPoint: {
                symbolSize: 1,
                symbolOffset: [0, '50%'],
                label: {
                   normal: {
                        formatter: '{a|{a}\n}{b|{b} }{c|{c}}',
                        backgroundColor: 'rgb(242,242,242)',
                        borderColor: '#aaa',
                        borderWidth: 1,
                        borderRadius: 4,
                        padding: [4, 10],
                        lineHeight: 26,
                        // shadowBlur: 5,
                        // shadowColor: '#000',
                        // shadowOffsetX: 0,
                        // shadowOffsetY: 1,
                        position: 'right',
                        distance: 20,
                        rich: {
                            a: {
                                align: 'center',
                                color: '#fff',
                                fontSize: 18,
                                textShadowBlur: 2,
                                textShadowColor: '#000',
                                textShadowOffsetX: 0,
                                textShadowOffsetY: 1,
                                textBorderColor: '#333',
                                textBorderWidth: 2
                            },
                            b: {
                                 color: '#333'
                            },
                            c: {
                                color: '#ff8811',
                                textBorderColor: '#000',
                                textBorderWidth: 1,
                                fontSize: 22
                            }
                        }
                   }
                },
                data: [
                    {type: 'max', name: 'max days: '},
                    {type: 'min', name: 'min days: '}
                ]
            }
        },
        {
            name: 'City Beta',
            type: 'bar',
            label: seriesLabel,
            data: [150, 105, 110]
        },
        {
            name: 'City Gamma',
            type: 'bar',
            label: seriesLabel,
            data: [220, 82, 63]
        }
    ]
};

        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option);
}


$(function(){
	//setChart1();
	setChart2();
	//setChart3(); 
	setChart4();
	setChart5();
    setChart6();
});