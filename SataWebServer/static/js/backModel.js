
function setPerformChart1(){
	// 基于准备好的dom，初始化echarts实例
     var myChart = echarts.init(document.getElementById('performChart1'));

    // 指定图表的配置项和数据

option = {
    title: {
        text: '模型训练损失值变化情况',
        //subtext: '纯属虚构'
    },
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
        data: ['10', '20', '30', '40', '50', '60', '70', '80', '90', '100', '110', '120', '130', '140', '150', '160', '170', '180', '190', '200']
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
//    visualMap: {
//        show: false,
//        dimension: 0,
//        pieces: [{
//            lte: 6,
//            color: 'green'
//        }, {
//            gt: 6,
//            lte: 8,
//            color: 'red'
//        }, {
//            gt: 8,
//            lte: 14,
//            color: 'green'
//        }, {
//            gt: 14,
//            lte: 17,
//            color: 'red'
//        }, {
//            gt: 17,
//            color: 'green'
//        }]
//    },
    series: [
        {
            name:'损失值',
            type:'line',
            smooth: true,
            data: [1.2, 1.11, 1.1, 1.0, 0.95, 0.92, 0.90, 0.88, 0.85, 0.83, 0.81, 0.79, 0.77, 0.76, 0.75, 0.74, 0.736, 0.735, 0.732, 0.731],
//            markArea: {
//                data: [ [{
//                    name: '早高峰',
//                    xAxis: '07:30'
//                }, {
//                    xAxis: '10:00'
//                }], [{
//                    name: '晚高峰',
//                    xAxis: '17:30'
//                }, {
//                    xAxis: '21:15'
//                }] ]
//            }
        }
    ]
};


	// 使用刚指定的配置项和数据显示图表。
    myChart.setOption(option);
};



$(function(){
	setPerformChart1();

});

$('datetimepicker').datetimepicker({

format:yyyy-mm-dd,

        weekStart: 1,

        todayBtn:  1,

autoclose: 1,

todayHighlight: 1,

startView: 2,

forceParse: 0,

        showMeridian: 1

    });