function setChart3_2(){

	// 基于准备好的dom，初始化echarts实例
     var myChart = echarts.init(document.getElementById('3-chart2'));

    // 指定图表的配置项和数据

option = {
    //title: {
    //    text: '企业接受资助情况'
    //},
    tooltip: {
        trigger: 'axis'
    },
    legend: {
        data:['福网信息科技','福赛特机器人','秀派电子科技','今日头条']
    },
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },
//    toolbox: {
//        feature: {
//            saveAsImage: {}
//        }
//    },
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
            name:'福网信息科技',
            type:'line',
            stack: '总量',
            data:[120, 132, 101, 134, 90, 230, 210]
        },
        {
            name:'福赛特机器人',
            type:'line',
            stack: '总量',
            data:[220, 182, 191, 234, 290, 330, 310]
        },
        {
            name:'秀派电子科技',
            type:'line',
            stack: '总量',
            data:[150, 232, 201, 154, 190, 330, 410]
        },
        {
            name:'今日头条',
            type:'line',
            stack: '总量',
            data:[320, 332, 301, 334, 390, 330, 320]
        }
    ]
};


	// 使用刚指定的配置项和数据显示图表。
    myChart.setOption(option);
	
}

function setChart1_1(){

	// 基于准备好的dom，初始化echarts实例
     var myChart = echarts.init(document.getElementById('1-chart1'));

    // 指定图表的配置项和数据

option = {
    //title: {
    //    text: '企业接受资助情况'
    //},
    tooltip: {
        trigger: 'axis'
    },
    legend: {
        data:['福网信息科技','福赛特机器人','秀派电子科技','今日头条']
    },
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },
//    toolbox: {
//        feature: {
//            saveAsImage: {}
//        }
//    },
    xAxis: {
        type: 'category',
        boundaryGap: false,
        data: ['2015','2016','2017','2018']
    },
    yAxis: {
        type: 'value'
    },
    series: [
        {
            name:'福网信息科技',
            type:'line',
            stack: '福网信息科技',
            data:[2665.08, 3528.41, 5192.77, 5688.41]
        },
        {
            name:'福赛特机器人',
            type:'line',
            stack: '福赛特机器人',
            data:[766.84, 665.82, 1898.50, 2198.50]
        },
        {
            name:'秀派电子科技',
            type:'line',
            stack: '秀派电子科技',
            data:[3880, 3533, 4021, 3940]
        },
        {
            name:'今日头条',
            type:'line',
            stack: '今日头条',
            data:[3200, 3320, 3010, 3340]
        }
    ]
};


	// 使用刚指定的配置项和数据显示图表。
    myChart.setOption(option);
	
}

function setChart1_2(){

	// 基于准备好的dom，初始化echarts实例
     var myChart = echarts.init(document.getElementById('1-chart2'));

    // 指定图表的配置项和数据

option = {
    //title: {
    //    text: '企业接受资助情况'
    //},
    tooltip: {
        trigger: 'axis'
    },
    legend: {
        data:['福网信息科技','福赛特机器人','秀派电子科技','今日头条']
    },
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },
//    toolbox: {
//        feature: {
//            saveAsImage: {}
//        }
//    },
    xAxis: {
        type: 'category',
        boundaryGap: false,
        data: ['2015','2016','2017','2018']
    },
    yAxis: {
        type: 'value'
    },
    series: [
        {
            name:'福网信息科技',
            type:'line',
            stack: '福网信息科技',
            data:[120, 132, 101, 134]
        },
        {
            name:'福赛特机器人',
            type:'line',
            stack: '福赛特机器人',
            data:[220, 182, 191, 234]
        },
        {
            name:'秀派电子科技',
            type:'line',
            stack: '秀派电子科技',
            data:[150, 232, 201, 154]
        },
        {
            name:'今日头条',
            type:'line',
            stack: '今日头条',
            data:[320, 332, 301, 334]
        }
    ]
};

	// 使用刚指定的配置项和数据显示图表。
    myChart.setOption(option);
	
}


function setChart1_3(){

	// 基于准备好的dom，初始化echarts实例
     var myChart = echarts.init(document.getElementById('1-chart3'));

    // 指定图表的配置项和数据

option = {
    //title: {
    //    text: '企业接受资助情况'
    //},
    tooltip: {
        trigger: 'axis'
    },
    legend: {
        data:['福网信息科技','福赛特机器人','秀派电子科技','今日头条']
    },
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },
//    toolbox: {
//        feature: {
//            saveAsImage: {}
//        }
//    },
    xAxis: {
        type: 'category',
        boundaryGap: false,
        data: ['2015','2016','2017','2018']
    },
    yAxis: {
        type: 'value'
    },
    series: [
        {
            name:'福网信息科技',
            type:'line',
            stack: '福网信息科技',
            data:[1908.77,2873.11,7185.50,8450.1]
        },
        {
            name:'福赛特机器人',
            type:'line',
            stack: '福赛特机器人',
            data:[1021, 279.27, 289.27, 475]
        },
        {
            name:'秀派电子科技',
            type:'line',
            stack: '秀派电子科技',
            data:[2951.0, 3011, 3425, 2430]
        },
        {
            name:'今日头条',
            type:'line',
            stack: '今日头条',
            data:[3202, 3322, 3301, 3534]
        }
    ]
};


	// 使用刚指定的配置项和数据显示图表。
    myChart.setOption(option);
	
} // end of set chart1-3


function setChart2_1(){

	// 基于准备好的dom，初始化echarts实例
     var myChart = echarts.init(document.getElementById('2-chart1'));

    // 指定图表的配置项和数据

option = {
    //title: {
    //    text: '企业接受资助情况'
    //},
    tooltip: {
        trigger: 'axis'
    },
    legend: {
        data:['福网信息科技','福赛特机器人','秀派电子科技','今日头条']
    },
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },
//    toolbox: {
//        feature: {
//            saveAsImage: {}
//        }
//    },
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
            name:'福网信息科技',
            type:'line',
            stack: '总量',
            data:[120, 132, 101, 134, 90, 230, 210]
        },
        {
            name:'福赛特机器人',
            type:'line',
            stack: '总量',
            data:[220, 182, 191, 234, 290, 330, 310]
        },
        {
            name:'秀派电子科技',
            type:'line',
            stack: '总量',
            data:[150, 232, 201, 154, 190, 330, 410]
        },
        {
            name:'今日头条',
            type:'line',
            stack: '总量',
            data:[320, 332, 301, 334, 390, 330, 320]
        }
    ]
};


	// 使用刚指定的配置项和数据显示图表。
    myChart.setOption(option);
	
} // end of set chart2-1

function setChart2_2(){

	// 基于准备好的dom，初始化echarts实例
     var myChart = echarts.init(document.getElementById('2-chart2'));

    // 指定图表的配置项和数据

option = {
    //title: {
    //    text: '企业接受资助情况'
    //},
    tooltip: {
        trigger: 'axis'
    },
    legend: {
        data:['福网信息科技','福赛特机器人','秀派电子科技','今日头条']
    },
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },
//    toolbox: {
//        feature: {
//            saveAsImage: {}
//        }
//    },
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
            name:'福网信息科技',
            type:'line',
            stack: '总量',
            data:[120, 132, 101, 134, 90, 230, 210]
        },
        {
            name:'福赛特机器人',
            type:'line',
            stack: '总量',
            data:[220, 182, 191, 234, 290, 330, 310]
        },
        {
            name:'秀派电子科技',
            type:'line',
            stack: '总量',
            data:[150, 232, 201, 154, 190, 330, 410]
        },
        {
            name:'今日头条',
            type:'line',
            stack: '总量',
            data:[320, 332, 301, 334, 390, 330, 320]
        }
    ]
};


	// 使用刚指定的配置项和数据显示图表。
    myChart.setOption(option);
	
} // end of set chart2-2

function setChart2_3(){

	// 基于准备好的dom，初始化echarts实例
     var myChart = echarts.init(document.getElementById('2-chart3'));

    // 指定图表的配置项和数据

option = {
    //title: {
    //    text: '企业接受资助情况'
    //},
    tooltip: {
        trigger: 'axis'
    },
    legend: {
        data:['福网信息科技','福赛特机器人','秀派电子科技','今日头条']
    },
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },
//    toolbox: {
//        feature: {
//            saveAsImage: {}
//        }
//    },
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
            name:'福网信息科技',
            type:'line',
            stack: '总量',
            data:[120, 132, 101, 134, 90, 230, 210]
        },
        {
            name:'福赛特机器人',
            type:'line',
            stack: '总量',
            data:[220, 182, 191, 234, 290, 330, 310]
        },
        {
            name:'秀派电子科技',
            type:'line',
            stack: '总量',
            data:[150, 232, 201, 154, 190, 330, 410]
        },
        {
            name:'今日头条',
            type:'line',
            stack: '总量',
            data:[320, 332, 301, 334, 390, 330, 320]
        }
    ]
};


	// 使用刚指定的配置项和数据显示图表。
    myChart.setOption(option);
	
} // end of set chart2-3

function setChart3_1(){

	// 基于准备好的dom，初始化echarts实例
     var myChart = echarts.init(document.getElementById('3-chart1'));

    // 指定图表的配置项和数据

option = {
    //title: {
    //    text: '企业接受资助情况'
    //},
    tooltip: {
        trigger: 'axis'
    },
    legend: {
        data:['福网信息科技','福赛特机器人','秀派电子科技','今日头条']
    },
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },
//    toolbox: {
//        feature: {
//            saveAsImage: {}
//        }
//    },
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
            name:'福网信息科技',
            type:'line',
            stack: '总量',
            data:[120, 132, 101, 134, 90, 230, 210]
        },
        {
            name:'福赛特机器人',
            type:'line',
            stack: '总量',
            data:[220, 182, 191, 234, 290, 330, 310]
        },
        {
            name:'秀派电子科技',
            type:'line',
            stack: '总量',
            data:[150, 232, 201, 154, 190, 330, 410]
        },
        {
            name:'今日头条',
            type:'line',
            stack: '总量',
            data:[320, 332, 301, 334, 390, 330, 320]
        }
    ]
};


	// 使用刚指定的配置项和数据显示图表。
    myChart.setOption(option);
	
} // end of set chart3-1

function setChart3_3(){

	// 基于准备好的dom，初始化echarts实例
     var myChart = echarts.init(document.getElementById('3-chart3'));

    // 指定图表的配置项和数据

option = {
    //title: {
    //    text: '企业接受资助情况'
    //},
    tooltip: {
        trigger: 'axis'
    },
    legend: {
        data:['福网信息科技','福赛特机器人','秀派电子科技','今日头条']
    },
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },
//    toolbox: {
//        feature: {
//            saveAsImage: {}
//        }
//    },
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
            name:'福网信息科技',
            type:'line',
            stack: '总量',
            data:[120, 132, 101, 134, 90, 230, 210]
        },
        {
            name:'福赛特机器人',
            type:'line',
            stack: '总量',
            data:[220, 182, 191, 234, 290, 330, 310]
        },
        {
            name:'秀派电子科技',
            type:'line',
            stack: '总量',
            data:[150, 232, 201, 154, 190, 330, 410]
        },
        {
            name:'今日头条',
            type:'line',
            stack: '总量',
            data:[320, 332, 301, 334, 390, 330, 320]
        }
    ]
};


	// 使用刚指定的配置项和数据显示图表。
    myChart.setOption(option);
	
} // end of set chart3-3




$(function(){
	//setChart1();
	//setChart2();
	//setChart3(); 
	//setChart4();
	setChart1_1();
    setChart1_2();
	setChart1_3();

	setChart2_1();
	setChart2_2();
	setChart2_3();


	setChart3_1();
	setChart3_2();
	setChart3_3();
});

function queryButton(){
 //alert('ok');
 regionPicker = document.getElementById('regionClassPicker');
 industPicker = document.getElementById('industryClassPicker');
 timePicker = document.getElementById('timeClassPicker');
 searchCom = document.getElementById('comName');
 selectRegion = regionPicker.options[regionPicker.selectedIndex].value;
 selectTime = timePicker.options[timePicker.selectedIndex].value;
 selectIndust = industPicker.options[industPicker.selectedIndex].value;
 searchComName = searchCom.value;
 //alert(searchComName);

$.post("govPolicyMicroCom/comInfo", {'region':selectRegion, 'time':selectTime, 'industType':selectIndust,'searchComName': searchComName}, function(ret){

	//alert('okkkk')
	comInfo = ret['comInfo']
	var tab1=document.getElementById('queryTab');
	alert(tab1.rows.length)

	// 清空表格
	elemNum = tab1.rows.length-1
	for (i=0;i< elemNum; i++)
	{
		tab1.deleteRow(1)
	}

	// 添加元素
	for (i=0;i<comInfo.length ;i++ )
	{
		com = comInfo[i]
		var tradd=tab1.insertRow(1)
        tradd.innerHTML='<td>'+com[0]+'</td><td>'+com[1]+'</td><td>'+com[2]+'</td><td><button type="button" class="btn btn-secondary" onclick="addButton(this)">添加</button></td>'   
	}

});

}

function addButton(elem){
		col = elem.parentNode;
		r = col.parentNode;
		alert(r.rowIndex);
		rIndex = r.rowIndex;
		rContent = r.innerHTML;
		cells = r.cells
		//alert(r.cells.length)
	    //alert(cells[1].innerHTML)
		comID = cells[0].innerHTML
		comName = cells[1].innerHTML
		comRegion = cells[2].innerHTML

        var tab2=document.getElementById('compareTab');
        var tradd=tab2.insertRow(1)
        tradd.innerHTML='<td>'+comID+'</td><td>'+comName+'</td><td>'+comRegion+'</td><td><button type="button" class="btn btn-secondary" onclick="deleteButton(this)">删除</button></td>'   
};

function deleteButton(elem){
		col = elem.parentNode;
		r = col.parentNode;
		alert(r.rowIndex)
		rIndex = r.rowIndex
		tab2=document.getElementById("compareTab")
		tab2.deleteRow(rIndex) 
};

function refreshButton(){

	var timeSelectMin = document.getElementById('timeMin');
	timeMin = timeSelectMin.options[timeSelectMin.selectedIndex].value
	var timeSelectMax = document.getElementById('timeMax');
	timeMax = timeSelectMax.options[timeSelectMax.selectedIndex].value
	if (timeMin>timeMax)
	{
		alert("起始时间要晚于终止时间");
		return false;
	}
	var tab2=document.getElementById('compareTab');
	rows = tab2.rows
	elemNum = rows.length-1
	comIdList = []
	comNameList0 = []
	for (i=1;i< elemNum+1; i++)
	{
		comId = rows[i].cells[0].innerHTML;
		comIdList.push(comId);
		comName = rows[i].cells[1].innerHTML;
		comNameList0.push(comName);
	}

	
	if (comIdList.length==0)
	{
		return false;
	}
	alert(comIdList);
	
	$.post("govPolicyMicroCom/comFinance", {'timeMin':timeMin, 'timeMax':timeMax, 'comIdList':JSON.stringify(comIdList)}, function(ret){
		alert('get com finance info');

		//comNameList = ret['comNameList'];
		comNameList = comNameList0;
		alert(comNameList);
		yearList = ret['yearList'];
		totalIncomeData = ret['totalIncomeData'];
		totalReliefData = ret['totalReliefData'];
		totalIncreaseData = ret['totalIncreaseData']

		// set chart 4
		// 基于准备好的dom，初始化echarts实例

		sData = []
		for (i=0;i<totalReliefData.length ; i++ )
		{
			d={
            name:comNameList[i],
            type:'line',
            stack: comNameList[i],
            data:totalReliefData[i]
			}
			sData.push(d)
		}
     var myChart = echarts.init(document.getElementById('3-chart2'));//.clear()

    // 指定图表的配置项和数据

	option = {
    //title: {
    //    text: '企业接受资助情况'
    //},
    tooltip: {
        trigger: 'axis'
    },
    legend: {
        data:comNameList
    },
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },
//    toolbox: {
//        feature: {
//            saveAsImage: {}
//        }
//    },
    xAxis: {
        type: 'category',
        boundaryGap: false,
        data: yearList
    },
    yAxis: {
        type: 'value'
    },
    series: sData
};
	// 使用刚指定的配置项和数据显示图表。true是说重新绘制
    myChart.setOption(option,true);


		// set chart 5
		// 基于准备好的dom，初始化echarts实例

				sData = []
		for (i=0;i<totalIncomeData.length ; i++ )
		{
			d={
            name:comNameList[i],
            type:'line',
            stack: comNameList[i],
            data:totalIncomeData[i]
			}
			sData.push(d)
		}
		//$("#chart5").empty();
     var myChart = echarts.init(document.getElementById('1-chart1'));//.clear()

    // 指定图表的配置项和数据

	option = {
    //title: {
    //    text: '企业接受资助情况'
    //},
    tooltip: {
        trigger: 'axis'
    },
    legend: {
        data:comNameList
    },
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },
//    toolbox: {
//        feature: {
//            saveAsImage: {}
//        }
//    },
    xAxis: {
        type: 'category',
        boundaryGap: false,
        data: yearList
    },
    yAxis: {
        type: 'value'
    },
    series: sData
};
	// 使用刚指定的配置项和数据显示图表。true是说重新绘制
    myChart.setOption(option,true);


		// set chart 6
		// 基于准备好的dom，初始化echarts实例

				sData = []
		for (i=0;i<totalIncreaseData.length ; i++ )
		{
			d={
            name:comNameList[i],
            type:'line',
            stack: comNameList[i],
            data:totalIncreaseData[i]
			}
			sData.push(d)
		}
		//$("#chart5").empty();
     var myChart = echarts.init(document.getElementById('1-chart2'));//.clear()

    // 指定图表的配置项和数据

	option = {
    //title: {
    //    text: '企业接受资助情况'
    //},
    tooltip: {
        trigger: 'axis'
    },
    legend: {
        data:comNameList
    },
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },
//    toolbox: {
//        feature: {
//            saveAsImage: {}
//        }
//    },
    xAxis: {
        type: 'category',
        boundaryGap: false,
        data: yearList
    },
    yAxis: {
        type: 'value'
    },
    series: sData
};
	// 使用刚指定的配置项和数据显示图表。true是说重新绘制
    myChart.setOption(option,true);


	});// end of post
};
