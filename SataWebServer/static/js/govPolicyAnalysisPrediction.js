function setChart1(){
	// 基于准备好的dom，初始化echarts实例
     var myChart = echarts.init(document.getElementById('chart1'));

    // 指定图表的配置项和数据

option = {
    //title: {
    //    text: '企业接受资助情况'
    //},
    tooltip: {
        trigger: 'axis'
    },
    legend: {
        data:['腾讯','阿里','百度','今日头条','大众点评']
    },
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },
    toolbox: {
        feature: {
            saveAsImage: {}
        }
    },
    xAxis: {
        type: 'category',
        boundaryGap: false,
        data: ['2014','2015','2016','2017','2018','2019','2020']
    },
    yAxis: {
        type: 'value'
    },
    series: [
        {
            name:'腾讯',
            type:'line',
            stack: '总量',
            data:[120, 132, 101, 134, 90, 230, 210]
        },
        {
            name:'阿里',
            type:'line',
            stack: '总量',
            data:[220, 182, 191, 234, 290, 330, 310]
        },
        {
            name:'百度',
            type:'line',
            stack: '总量',
            data:[150, 232, 201, 154, 190, 330, 410]
        },
        {
            name:'今日头条',
            type:'line',
            stack: '总量',
            data:[320, 332, 301, 334, 390, 330, 320]
        },
        {
            name:'大众点评',
            type:'line',
            stack: '总量',
            data:[820, 932, 901, 934, 1290, 1330, 1320]
        }
    ]
};


	// 使用刚指定的配置项和数据显示图表。
    myChart.setOption(option);
}

function setChart2(){
		// 基于准备好的dom，初始化echarts实例
     var myChart = echarts.init(document.getElementById('chart2'));

    // 指定图表的配置项和数据

option = {
    //title: {
    //    text: '企业接受资助情况'
    //},
    tooltip: {
        trigger: 'axis'
    },
    legend: {
        data:['腾讯','阿里','百度','今日头条','大众点评']
    },
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },
    toolbox: {
        feature: {
            saveAsImage: {}
        }
    },
    xAxis: {
        type: 'category',
        boundaryGap: false,
        data: ['2014','2015','2016','2017','2018','2019','2020']
    },
    yAxis: {
        type: 'value'
    },
    series: [
        {
            name:'腾讯',
            type:'line',
            stack: '总量',
            data:[120, 132, 101, 134, 90, 230, 210]
        },
        {
            name:'阿里',
            type:'line',
            stack: '总量',
            data:[220, 182, 191, 234, 290, 330, 310]
        },
        {
            name:'百度',
            type:'line',
            stack: '总量',
            data:[150, 232, 201, 154, 190, 330, 410]
        },
        {
            name:'今日头条',
            type:'line',
            stack: '总量',
            data:[320, 332, 301, 334, 390, 330, 320]
        },
        {
            name:'大众点评',
            type:'line',
            stack: '总量',
            data:[820, 932, 901, 934, 1290, 1330, 1320]
        }
    ]
};


	// 使用刚指定的配置项和数据显示图表。
    myChart.setOption(option);
}

function setChart3(){
	// 基于准备好的dom，初始化echarts实例
     var myChart = echarts.init(document.getElementById('chart3'));

    // 指定图表的配置项和数据

option = {
    //title: {
    //    text: '一天用电量分布',
    //    subtext: '纯属虚构'
    //},
    tooltip: {
        trigger: 'axis',
        axisPointer: {
            type: 'cross'
        }
    },
    toolbox: {
        show: true,
        feature: {
            saveAsImage: {}
        }
    },
    xAxis:  {
        type: 'category',
        boundaryGap: false,
        data: ['00:00', '01:15', '02:30', '03:45', '05:00', '06:15', '07:30', '08:45', '10:00', '11:15', '12:30', '13:45', '15:00', '16:15', '17:30', '18:45', '20:00', '21:15', '22:30', '23:45']
    },
    yAxis: {
        type: 'value',
        axisLabel: {
            formatter: '{value} W'
        },
        axisPointer: {
            snap: true
        }
    },
    visualMap: {
        show: false,
        dimension: 0,
        pieces: [{
            lte: 6,
            color: 'green'
        }, {
            gt: 6,
            lte: 8,
            color: 'red'
        }, {
            gt: 8,
            lte: 14,
            color: 'green'
        }, {
            gt: 14,
            lte: 17,
            color: 'red'
        }, {
            gt: 17,
            color: 'green'
        }]
    },
    series: [
        {
            name:'增长率',
            type:'line',
            smooth: true,
            data: [300, 280, 250, 260, 270, 300, 550, 500, 400, 390, 380, 390, 400, 500, 600, 750, 800, 700, 600, 400],
            markArea: {
                data: [ [{
                    name: '评为高新企业',
                    xAxis: '06:15'
                }, {
                    xAxis: '07:30'
                }], [{
                    name: '补贴10%',
                    xAxis: '17:30'
                }, {
                    xAxis: '20:00'
                }] ]
            }
        }
    ]
};


	// 使用刚指定的配置项和数据显示图表。
    myChart.setOption(option);
}


$(function(){
	setChart1();
	setChart2();
	setChart3(); 
//	setChart4();
//	setChart5();
//  setChart6();
});