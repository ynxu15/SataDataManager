


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

// 点击操作，更新图
function updateLineChart(myChartId, legendData, xAxisData, seriesData){

	// 基于准备好的dom，初始化echarts实例
     var myChart = echarts.init(document.getElementById(myChartId));

    // 指定图表的配置项和数据
	sData = [];
	for (i=0; i<seriesData.length; i++)
	{
		d = {
            name:legendData[i],
            type:'line',
            stack: '总量',
            data:seriesData[i]
        }
		sData.push(d);
	}

//alert(legendData);

option = {
    //title: {
    //    text: '企业接受资助情况'
    //},
    tooltip: {
        trigger: 'axis'
    },
    legend: {
        data:legendData
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
        data: xAxisData
    },
    yAxis: {
        type: 'value'
    },
    series: sData
}; // end of option


	// 使用刚指定的配置项和数据显示图表。
    myChart.setOption(option, true);
	

}// end of changeLineChart

// 查询按钮操作
function qButtonClick(){

 timePicker1 = document.getElementById('timeClassPickerQMin');
 timePicker2 = document.getElementById('timeClassPickerQMax');
 regionPicker = document.getElementById('regionClassPicker');
 industPicker = document.getElementById('industryClassPicker');
 selectRegion = regionPicker.options[regionPicker.selectedIndex].value;
 selectTimeMin = timePicker1.options[timePicker1.selectedIndex].value;
 selectTimeMax = timePicker2.options[timePicker2.selectedIndex].value;
 selectIndust = industPicker.options[industPicker.selectedIndex].value;

 $.post("govPolicyMacroTime/regionInfoQuery", {'selectRegion':selectRegion, 'selectTimeMin':selectTimeMin, 'selectTimeMax':selectTimeMax,'selectIndust':selectIndust}, function(ret){
	legendData = ret['legendData']
	xAxisData = ret['xAxisData']
	taxReliefSData = ret['taxReliefSData']
	incomeSData = ret['incomeSData']
	increaseSData = ret['increaseSData']
	
	// 更新图表
	updateLineChart("chart1", legendData, xAxisData, taxReliefSData);
	updateLineChart("chart4", legendData, xAxisData, incomeSData)
	updateLineChart("chart7", legendData, xAxisData, increaseSData)
	
}); // end of post

} // end of qButtonClick



function updateRadarChart(myChartId, legendData, xAxisData, seriesData){

	// 基于准备好的dom，初始化echarts实例
     var myChart = echarts.init(document.getElementById(myChartId));

    // 指定图表的配置项和数据
	sData = [];
	for (i=0; i<seriesData.length; i++)
	{
		d = {
        type: 'bar',
        data: seriesData[i],
        coordinateSystem: 'polar',
        name: legendData[i],
        stack: 'a'
		}
		sData.push(d);
	}

	option = {
		tooltip: {
        trigger: 'axis'
		},
		angleAxis: {
			type: 'category',
			data: xAxisData,
			//z: 10
		},
		radiusAxis: {
		},
		polar: {
		},
		series: sData,
		legend: {
			show: true,
			data: legendData
		}
	};// end of option


	// 使用刚指定的配置项和数据显示图表。
    myChart.setOption(option, true);

}// end of changeLineChart


// 比较按钮操作
function cButtonClick(){

 timePicker1 = document.getElementById('timeClassPickerC1');
 timePicker2 = document.getElementById('timeClassPickerC2');
 regionPicker = document.getElementById('regionClassPicker');
 industPicker = document.getElementById('industryClassPicker');

 selectTime1 = timePicker1.options[timePicker1.selectedIndex].value;
 selectTime2 = timePicker2.options[timePicker2.selectedIndex].value;
 selectRegion = regionPicker.options[regionPicker.selectedIndex].value;
 selectIndust = industPicker.options[industPicker.selectedIndex].value;

 $.post("govPolicyMacroTime/regionInfoCompare", {'selectRegion':selectRegion, 'selectTime1':selectTime1, 'selectTime2':selectTime2,'selectIndust':selectIndust}, function(ret){
	legendData = ret['legendData']
	xAxisData = ret['xAxisData']
	taxReliefSData1 = ret['taxReliefSData1']
	taxReliefSData2 = ret['taxReliefSData2']
	incomeSData1 = ret['incomeSData1']
	incomeSData2 = ret['incomeSData2']
	increaseSData1 = ret['increaseSData1']
	increaseSData2 = ret['increaseSData2']

	alert(increaseSData1);
	
	// 更新图表
	updateRadarChart("chart2", legendData, xAxisData, taxReliefSData1);
	updateRadarChart("chart3", legendData, xAxisData, taxReliefSData2);
	updateRadarChart("chart5", legendData, xAxisData, incomeSData1);
	updateRadarChart("chart6", legendData, xAxisData, incomeSData2);
	updateRadarChart("chart8", legendData, xAxisData, increaseSData1);
	updateRadarChart("chart9", legendData, xAxisData, increaseSData2);
	
}); // end of post


} // end of cButtonClick


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