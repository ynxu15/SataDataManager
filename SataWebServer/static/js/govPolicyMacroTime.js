


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
        data:['互联网企业','机械制造','加工业','旅游业','外贸']
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
            name:'互联网企业',
            type:'line',
            stack: '总量',
            data:[120, 132, 101, 134, 90, 230, 210]
        },
        {
            name:'机械制造',
            type:'line',
            stack: '总量',
            data:[220, 182, 191, 234, 290, 330, 310]
        },
        {
            name:'加工业',
            type:'line',
            stack: '总量',
            data:[150, 232, 201, 154, 190, 330, 410]
        },
        {
            name:'旅游业',
            type:'line',
            stack: '总量',
            data:[320, 332, 301, 334, 390, 330, 320]
        },
        {
            name:'外贸',
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

	//app.title = '极坐标系下的堆叠柱状图';

option = {
    angleAxis: {
        type: 'category',
        data: ['徐家汇', '闵行区', '松江区', '奉贤区', '浦东新区', '金山区', '青浦区'],
        z: 10
    },
    radiusAxis: {
    },
    polar: {
    },
    series: [{
        type: 'bar',
        data: [1, 2, 3, 4, 3, 5, 1],
        coordinateSystem: 'polar',
        name: '互联网行业',
        stack: 'a'
    }, {
        type: 'bar',
        data: [2, 4, 6, 1, 3, 2, 1],
        coordinateSystem: 'polar',
        name: '机械制造',
        stack: 'a'
    }, {
        type: 'bar',
        data: [1, 2, 3, 4, 1, 2, 5],
        coordinateSystem: 'polar',
        name: '加工业',
        stack: 'a'
    }],
    legend: {
        show: true,
        data: ['互联网行业', '机械制造', '加工业']
    }
};
        
        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option);
}

function setChart3(){

	// 基于准备好的dom，初始化echarts实例
     var myChart = echarts.init(document.getElementById('chart3'));

	//app.title = '极坐标系下的堆叠柱状图';

option = {
    angleAxis: {
        type: 'category',
        data: ['徐家汇', '闵行区', '松江区', '奉贤区', '浦东新区', '金山区', '青浦区'],
        z: 10
    },
    radiusAxis: {
    },
    polar: {
    },
    series: [{
        type: 'bar',
        data: [1, 2, 3, 4, 3, 5, 1],
        coordinateSystem: 'polar',
        name: '互联网行业',
        stack: 'a'
    }, {
        type: 'bar',
        data: [2, 4, 6, 1, 3, 2, 1],
        coordinateSystem: 'polar',
        name: '机械制造',
        stack: 'a'
    }, {
        type: 'bar',
        data: [1, 2, 3, 4, 1, 2, 5],
        coordinateSystem: 'polar',
        name: '加工业',
        stack: 'a'
    }],
    legend: {
        show: true,
        data: ['互联网行业', '机械制造', '加工业']
    }
};
        
        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option);
}

function setChart4(){
// 基于准备好的dom，初始化echarts实例
     var myChart = echarts.init(document.getElementById('chart4'));

    // 指定图表的配置项和数据

option = {
    //title: {
    //    text: '企业接受资助情况'
    //},
    tooltip: {
        trigger: 'axis'
    },
    legend: {
        data:['互联网企业','机械制造','加工业','旅游业','外贸']
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
            name:'互联网企业',
            type:'line',
            stack: '总量',
            data:[120, 132, 101, 134, 90, 230, 210]
        },
        {
            name:'机械制造',
            type:'line',
            stack: '总量',
            data:[220, 182, 191, 234, 290, 330, 310]
        },
        {
            name:'加工业',
            type:'line',
            stack: '总量',
            data:[150, 232, 201, 154, 190, 330, 410]
        },
        {
            name:'旅游业',
            type:'line',
            stack: '总量',
            data:[320, 332, 301, 334, 390, 330, 320]
        },
        {
            name:'外贸',
            type:'line',
            stack: '总量',
            data:[820, 932, 901, 934, 1290, 1330, 1320]
        }
    ]
};


	// 使用刚指定的配置项和数据显示图表。
    myChart.setOption(option);
	
	
}

function setChart5(){
	// 基于准备好的dom，初始化echarts实例
     var myChart = echarts.init(document.getElementById('chart5'));

	//app.title = '极坐标系下的堆叠柱状图';

option = {
    angleAxis: {
        type: 'category',
        data: ['徐家汇', '闵行区', '松江区', '奉贤区', '浦东新区', '金山区', '青浦区'],
        z: 10
    },
    radiusAxis: {
    },
    polar: {
    },
    series: [{
        type: 'bar',
        data: [1, 2, 3, 4, 3, 5, 1],
        coordinateSystem: 'polar',
        name: '互联网行业',
        stack: 'a'
    }, {
        type: 'bar',
        data: [2, 4, 6, 1, 3, 2, 1],
        coordinateSystem: 'polar',
        name: '机械制造',
        stack: 'a'
    }, {
        type: 'bar',
        data: [1, 2, 3, 4, 1, 2, 5],
        coordinateSystem: 'polar',
        name: '加工业',
        stack: 'a'
    }],
    legend: {
        show: true,
        data: ['互联网行业', '机械制造', '加工业']
    }
};
        
        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option);
	
}

function setChart6(){

	// 基于准备好的dom，初始化echarts实例
     var myChart = echarts.init(document.getElementById('chart6'));

	//app.title = '极坐标系下的堆叠柱状图';

option = {
    angleAxis: {
        type: 'category',
        data: ['徐家汇', '闵行区', '松江区', '奉贤区', '浦东新区', '金山区', '青浦区'],
        z: 10
    },
    radiusAxis: {
    },
    polar: {
    },
    series: [{
        type: 'bar',
        data: [1, 2, 3, 4, 3, 5, 1],
        coordinateSystem: 'polar',
        name: '互联网行业',
        stack: 'a'
    }, {
        type: 'bar',
        data: [2, 4, 6, 1, 3, 2, 1],
        coordinateSystem: 'polar',
        name: '机械制造',
        stack: 'a'
    }, {
        type: 'bar',
        data: [1, 2, 3, 4, 1, 2, 5],
        coordinateSystem: 'polar',
        name: '加工业',
        stack: 'a'
    }],
    legend: {
        show: true,
        data: ['互联网行业', '机械制造', '加工业']
    }
};
        
        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option);


}

function setChart7(){
// 基于准备好的dom，初始化echarts实例
     var myChart = echarts.init(document.getElementById('chart7'));

    // 指定图表的配置项和数据

option = {
    //title: {
    //    text: '企业接受资助情况'
    //},
    tooltip: {
        trigger: 'axis'
    },
    legend: {
        data:['互联网企业','机械制造','加工业','旅游业','外贸']
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
            name:'互联网企业',
            type:'line',
            stack: '总量',
            data:[120, 132, 101, 134, 90, 230, 210]
        },
        {
            name:'机械制造',
            type:'line',
            stack: '总量',
            data:[220, 182, 191, 234, 290, 330, 310]
        },
        {
            name:'加工业',
            type:'line',
            stack: '总量',
            data:[150, 232, 201, 154, 190, 330, 410]
        },
        {
            name:'旅游业',
            type:'line',
            stack: '总量',
            data:[320, 332, 301, 334, 390, 330, 320]
        },
        {
            name:'外贸',
            type:'line',
            stack: '总量',
            data:[820, 932, 901, 934, 1290, 1330, 1320]
        }
    ]
};


	// 使用刚指定的配置项和数据显示图表。
    myChart.setOption(option);
	
	
}

function setChart8(){
		// 基于准备好的dom，初始化echarts实例
     var myChart = echarts.init(document.getElementById('chart8'));

	//app.title = '极坐标系下的堆叠柱状图';

option = {
    angleAxis: {
        type: 'category',
        data: ['徐家汇', '闵行区', '松江区', '奉贤区', '浦东新区', '金山区', '青浦区'],
        z: 10
    },
    radiusAxis: {
    },
    polar: {
    },
    series: [{
        type: 'bar',
        data: [1, 2, 3, 4, 3, 5, 1],
        coordinateSystem: 'polar',
        name: '互联网行业',
        stack: 'a'
    }, {
        type: 'bar',
        data: [2, 4, 6, 1, 3, 2, 1],
        coordinateSystem: 'polar',
        name: '机械制造',
        stack: 'a'
    }, {
        type: 'bar',
        data: [1, 2, 3, 4, 1, 2, 5],
        coordinateSystem: 'polar',
        name: '加工业',
        stack: 'a'
    }],
    legend: {
        show: true,
        data: ['互联网行业', '机械制造', '加工业']
    }
};
        
        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option);
	
}

function setChart9(){

	// 基于准备好的dom，初始化echarts实例
     var myChart = echarts.init(document.getElementById('chart9'));

	//app.title = '极坐标系下的堆叠柱状图';

option = {
    angleAxis: {
        type: 'category',
        data: ['徐家汇', '闵行区', '松江区', '奉贤区', '浦东新区', '金山区', '青浦区'],
        z: 10
    },
    radiusAxis: {
    },
    polar: {
    },
    series: [{
        type: 'bar',
        data: [1, 2, 3, 4, 3, 5, 1],
        coordinateSystem: 'polar',
        name: '互联网行业',
        stack: 'a'
    }, {
        type: 'bar',
        data: [2, 4, 6, 1, 3, 2, 1],
        coordinateSystem: 'polar',
        name: '机械制造',
        stack: 'a'
    }, {
        type: 'bar',
        data: [1, 2, 3, 4, 1, 2, 5],
        coordinateSystem: 'polar',
        name: '加工业',
        stack: 'a'
    }],
    legend: {
        show: true,
        data: ['互联网行业', '机械制造', '加工业']
    }
};
        
        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option);

}





$(function(){
	setChart1();
	setChart2();
	setChart3(); 
	setChart4();
	setChart5();
    setChart6();
	setChart7();
	setChart8();
	setChart9();
});