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
        data:['腾讯']
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
        data: ['2017','2018','2019','2020','2021','2022']
    },
    yAxis: {
        type: 'value'
    },
    series: [
        {
            name:'腾讯',
            type:'line',
            stack: '总量',
            data:[20, 32, 21, 34, 90, 100, 101]
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
    //    text: '企业接受资助情况'
    //},
    tooltip: {
        trigger: 'axis'
    },
    legend: {
        data:['原发展曲线','预测发展曲线']
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
        data: ['2017','2018','2019','2020','2021','2022','2023']
    },
    yAxis: {
        type: 'value'
    },
    series: [
        {
            name:'原发展曲线',
            type:'line',
            stack: '原发展曲线',
            data:[820, 932, 901, 934, 950, 955, 960]
        },
        {
            name:'预测发展曲线',
            type:'line',
            stack: '预测发展曲线',
            data:[820, 932, 901, 934, 1290, 1330, 1320]
        }
    ]
};


	// 使用刚指定的配置项和数据显示图表。
    myChart.setOption(option);
}

function setChart1(){
	// 基于准备好的dom，初始化echarts实例
     var myChart = echarts.init(document.getElementById('chart1'));

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
//    toolbox: {
//        show: true,
//        feature: {
//            saveAsImage: {}
//        }
//    },
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },
    xAxis:  {
        type: 'category',
        boundaryGap: false,
        data: ['2016.1', '2016.4', '2016.7', '2016.10', '2017.1', '2017.4', '2017.7', '2017.10', '2018.1', '2018.4', '2018.7', '2018.10']
    },
    yAxis: {
        type: 'value',
//        axisLabel: {
//            formatter: '{value} W'
//        },
        axisPointer: {
            snap: true
        }
    },
    visualMap: {
        show: false,
        dimension: 0,
        pieces: [{
            lte: 4,
            color: 'green'
        }, {
            gt: 4,
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
            name:'营收',
            type:'line',
            smooth: true,
            data: [800, 760, 770, 800, 1050, 1000, 900, 890, 880, 890, 900, 1000],
            markArea: {
                data: [ [{
                    name: '评为高新企业',
                    xAxis: '2016.10'
                }, {
                    xAxis: '2017.1'
                }], [{
                    name: '税收减免5%',
                    xAxis: '2018.7'
                }, {
                    xAxis: '2018.10'
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
//	setChart2();
//	setChart3(); 
//	setChart4();
//	setChart5();
//  setChart6();
});

	var symbolSize = 15;
    var data = [[2017, 20], [2018, 32], [2019, 21], [2020, 34], [2021, 90], [2022, 100], [2023, 101]];

    var myChart = echarts.init(document.getElementById('chart2'));

    myChart.setOption({
        tooltip: {
            triggerOn: 'none',
            formatter: function (params) {
                return 'X: ' + params.data[0].toFixed(2) + '<br>Y: ' + params.data[1].toFixed(2);
            }
        },
	    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
		},
        xAxis: {
            min: 2017,
            max: 2023,
            type: 'value',
            //axisLine: {onZero: false}
			splitLine:{show: false}
        },
        yAxis: {
            min: 0,
            max: 110,
            type: 'value',
            //axisLine: {onZero: false}
        },
        series: [
            {
                id: 'a',
                type: 'line',
                smooth: true,
                symbolSize: symbolSize,
                data: data
            }
        ],
    });

    myChart.setOption({
        graphic: echarts.util.map(data, function (item, dataIndex) {
            return {
                type: 'circle',
                position: myChart.convertToPixel('grid', item),
                shape: {
                    r: symbolSize / 2
                },
                invisible: true,
                draggable: true,
                ondrag: echarts.util.curry(onPointDragging, dataIndex),
                onmousemove: echarts.util.curry(showTooltip, dataIndex),
                onmouseout: echarts.util.curry(hideTooltip, dataIndex),
                z: 100
            };
        })
    });

    window.addEventListener('resize', function () {
        myChart.setOption({
            graphic: echarts.util.map(data, function (item, dataIndex) {
                return {
                    position: myChart.convertToPixel('grid', item)
                };
            })
        });
    });

    function showTooltip(dataIndex) {
        myChart.dispatchAction({
            type: 'showTip',
            seriesIndex: 0,
            dataIndex: dataIndex
        });
    }

    function hideTooltip(dataIndex) {
        myChart.dispatchAction({
            type: 'hideTip'
        });
    }

    function onPointDragging(dataIndex, dx, dy) {
        //data[dataIndex] = myChart.convertFromPixel('grid', this.position);
	    dt = myChart.convertFromPixel('grid', this.position);
		dt[0]= Math.round(dt[0]);
        data[dataIndex] = dt;

		//alert(dt);

        myChart.setOption({
            series: [{
                id: 'a',
                data: data
            }]
        });
    }


// chart 5
		// 基于准备好的dom，初始化echarts实例
var myChart1 = echarts.init(document.getElementById('chart3'));
originData = [820, 932, 901, 934, 950, 955, 960]
modifyData = [820, 932, 901, 934, 1290, 1330, 1320]

    // 指定图表的配置项和数据

option = {
    //title: {
    //    text: '企业接受资助情况'
    //},
    tooltip: {
        trigger: 'axis'
    },
    legend: {
        data:['原发展曲线','预测发展曲线']
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
        data: ['2017','2018','2019','2020','2021','2022','2023']
    },
    yAxis: {
        type: 'value'
    },
    series: [
        {
            name:'原发展曲线',
            type:'line',
            stack: '原发展曲线',
            data: originData
        },
        {
            name:'预测发展曲线',
            type:'line',
            stack: '预测发展曲线',
            data:modifyData
        }
    ]
};


	// 使用刚指定的配置项和数据显示图表。
    myChart1.setOption(option);

function modifyButton(){
	for (i=2;i<7 ;i++ )
	{
		modifyData[i] = originData[i] + 5*(data[i][1]-25)
	}
	s1= [
        {
            name:'原发展曲线',
            type:'line',
            stack: '原发展曲线',
            data: originData
        },
        {
            name:'预测发展曲线',
            type:'line',
            stack: '预测发展曲线',
            data:modifyData
        }
    ]
    myChart1.setOption({series:s1})
};