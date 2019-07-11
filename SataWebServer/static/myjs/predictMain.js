var dom = document.getElementById("container");
var myChart = echarts.init(dom);

option = null;

option = {
    title: {
        text: '上海市企业分布情况',
        textStyle: {
            fontSize: 26
        },
        subtext: '(点击跳转至对应区域发展情况分析)',
        subtextStyle: {
            fontSize: 16
        },
        left: 'center'
    },
    tooltip: {
        trigger: 'axis',
        axisPointer: { // 坐标轴指示器，坐标轴触发有效
            type: 'shadow' // 默认为直线，可选为：'line' | 'shadow'
        }
    },
    legend: {
        top: '7%',
        data: ['畜牧业', '食品制造业', '纺织业', '医药制造业', '金属制品业']
    },
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        top: '10%',
        containLabel: true
    },
    xAxis: {
        type: 'value'
    },
    yAxis: {
        type: 'category',
        data: ['黄浦', '徐汇', '长宁', '静安', '普陀', '虹口', '杨浦', '闵行', '宝山', '嘉定', '浦东', '金山', '松江', '青浦', '奉贤', '崇明']
    },
    series: [{
            name: '畜牧业',
            type: 'bar',
            stack: '总量',
            label: {
                normal: {
                    show: true,
                    position: 'insideRight'
                }
            },
            data: []
        },
        {
            name: '食品制造业',
            type: 'bar',
            stack: '总量',
            label: {
                normal: {
                    show: true,
                    position: 'insideRight'
                }
            },
            data: []
        },
        {
            name: '纺织业',
            type: 'bar',
            stack: '总量',
            label: {
                normal: {
                    show: true,
                    position: 'insideRight'
                }
            },
            data: []
        },
        {
            name: '医药制造业',
            type: 'bar',
            stack: '总量',
            label: {
                normal: {
                    show: true,
                    position: 'insideRight'
                }
            },
            data: []
        },
        {
            name: '金属制品业',
            type: 'bar',
            stack: '总量',
            label: {
                normal: {
                    show: true,
                    position: 'insideRight'
                }
            },
            data: []
        }
    ]
};

myChart.setOption(option, true);
$(document).ready(function () {
    $.getJSON("/flushMain/", {}, function (ret) {
        li = ret['data'];
        var data = new Array();
        for (var i = 0; i < 5; i++) {
            data[i] = new Array(i);
            for (var j = 0; j < 16; j++) {
                data[i][j] = i;
            }
        }
        for (var i = 0; i < 16; i++) {
            for (var j = 0; j < 5; j++) {
                data[j][i] = li[i * 5 + j]
            }
        }
        myChart.setOption({
            series: [{
                    data: data[0]
                }, {
                    data: data[1]
                }, {
                    data: data[2]
                }, {
                    data: data[3]
                }, {
                    data: data[4]
                }

            ]
        });
        myChart.on('click', function (params) {
            window.location.href = 'predictPart?region=' + encodeURIComponent(params.name) + '&type=全部'
        });
    })

})