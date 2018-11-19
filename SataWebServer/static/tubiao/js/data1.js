var  c1_option1 = {

    tooltip: {
        trigger: 'axis'
    },
    legend: {

        data:['RD支出','相当于GDP'],
        textStyle:{ color:'#fff'}
    },
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },

    xAxis: {
        type: 'category',
        boundaryGap: false,
        data: ['2012','2013','2014','2015','2016','2022'],

         axisLabel: {
                textStyle: {
                    color: '#637c9a'
                }
            },
            splitLine:{show:true , lineStyle:{color:'#0a2239',opacity:1 , type:'dashed'}  }
    },
   yAxis:[  {
       name:'(亿)',
        type: 'value', position: 'left',
             axisLabel: {
                textStyle: {
                    color: '#637c9a'
                }
            },
            axisTick:{show:false},
        splitLine:{show:false},
        axisLine:{ lineStyle:{color:'#637c99'}  },
    },
     {
        name:'(%)',
        type: 'value',
          min: 3.0,
         max:4.0,
        position:'right',
             axisLabel: {
                textStyle: {
                    color: '#637c9a'
                },
                   formatter: '{value} %'
            },
            axisTick:{show:false},
            splitNumber: 2,
            splitLine:{show:false}  ,
            axisLine:{ lineStyle:{color:'#637c99'}  },
    },
    ],
    series: [
        {
            name:'RD支出',
            type:'line',
            symbol:'circle',
            symbolSize:8,
            itemStyle:{ normal:{ color:'#32c0ac',borderColor:'#32c0ac'} },
            lineStyle: { normal: {color: "#32c0ac"  }},
            data:[679.46,  776.78, 861.95,936.14, 1049.32, 1600]
        },
        {
            name:'相当于GDP',
            type:'line',
            symbol:'circle',
            yAxisIndex:1,
            symbolSize:8,
             itemStyle:{ normal:{ color:'#108dda',borderColor:'#108dda'},  opacity:0},
             lineStyle: { normal: {color: "#108dda"  }
         },
            data:[3.31, 3.49, 3.58, 3.65, 3.72, 4.0 ]
        },

    ]
};


var c1_option2 = {

    tooltip: {
        trigger: 'axis'
    },

    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },

    xAxis: {
        type: 'category',
        boundaryGap: false,
        data: ['2010','2011','2012','2013','2014','2015','2016'],

         axisLabel: {
                textStyle: {
                    color: '#637c9a'
                }
            },
            splitLine:{show:true , lineStyle:{color:'#0a2239',opacity:1 , type:'dashed'}  }
    },
   yAxis:[  {
       name:'(家)',
        type: 'value', position: 'left',
             axisLabel: {
                textStyle: {
                    color: '#637c9a'
                }
            },

        splitLine:{show:false},
        axisLine:{ lineStyle:{color:'#637c99'}  },
    }
    ],
    series: [
        {

            type:'line',
            symbol:'circle',
            symbolSize:8,
            itemStyle:{ normal:{ color:'#32c0ac',borderColor:'#32c0ac'} },
            lineStyle: { normal: {color: "#32c0ac"  }},
            data:[115,116,122,129,137,146,149]
        }


    ]
};



var c1_option3 =  {

    tooltip: {
        trigger: 'axis'
    },
    legend: {

        data:['每万人口发明专利拥有量','增速'],
        textStyle:{ color:'#fff'}
    },
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },

    xAxis: {
        type: 'category',
        boundaryGap: true,
        data: ['2010','2011','2012','2013','2014','2015','2016'],

         axisLabel: {
                textStyle: {
                    color: '#637c9a'
                }
            },
            splitLine:{show:true , lineStyle:{color:'#0a2239',opacity:1 , type:'dashed'}  }
    },
   yAxis:[  {
       name:'(个)',
        type: 'value', position: 'left',
             axisLabel: {
                textStyle: {
                    color: '#637c9a'
                }
            },

        splitLine:{show:false},
        axisLine:{ lineStyle:{color:'#637c99'}  },
    },
     {
        name:'(%)',
        type: 'value',
          min: 15.0,
         max:30.0,
        position:'right',
             axisLabel: {
                textStyle: {
                    color: '#637c9a'
                },
                   formatter: '{value} %'
            },
            splitNumber: 2,
            splitLine:{show:false}  ,
            axisLine:{ lineStyle:{color:'#637c99'}  },
    },
    ],
    series: [
        {
            name:'每万人口发明专利拥有量',
            type:'bar',
            symbol:'circle',
            symbolSize:8,
            barWidth:20,
            itemStyle:{ normal:{ color:'#32c0ac',borderColor:'#32c0ac'} },
            lineStyle: { normal: {color: "#32c0ac"  }},
            data:[10.4,13.4,17.2,20.3,23.7,28.0,35.2]
        },
        {
            name:'增速',
            type:'line',
            symbol:'circle',
            yAxisIndex:1,
            xAxisIndex: 0,
            symbolSize:8,
             itemStyle:{
            normal:{ color:'#108dda',borderColor:'#108dda'},  opacity:0},
             lineStyle: { normal: {color: "#108dda"  }
         },

            data:[0,28.9,28.4,18.1,16.6,18.1,21.5]
        },

    ]
};


var  c2_option1 = {

    tooltip: {
        trigger: 'axis',
    },

    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true,
    },

    xAxis: {
        type: 'category',
        boundaryGap: false,
        data: ['2010','2011','2012','2013','2014','2015','2016'],

         axisLabel: {
                textStyle: {
                    color: '#637c9a'
                }
            },
            splitLine:{show:true , lineStyle:{color:'#0a2239',opacity:1 , type:'dashed'}  }
    },
   yAxis: {
       name:'(%)',
       min:0.6,
        type: 'value', position: 'left',
             axisLabel: {
                textStyle: {
                    color: '#637c9a'
                }
            },

        splitLine:{show:false},
        axisLine:{ lineStyle:{color:'#637c99'}  },
    },

    series: [
        {
            name:'比列',
            type:'line',
            symbol:'circle',
            symbolSize:8,
            smooth: true,

            itemStyle:{ normal:{ color:'#32c0ac',borderColor:'#32c0ac'} },
            lineStyle: { normal: {color: "#32c0ac"  }},
             areaStyle: {
                normal: {
                    color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                        offset: 0,
                        color: '#32bfab'
                    }, {
                        offset: 1,
                        color: 'rgba(0,0,0,0)'
                    }]),

                    shadowBlur: 20,
                    opacity:0.2,
                },

            },
            data:[0.85, 1,1.09,1.17,1.27,1.39,1.43]
        },

    ]
};

var c2_option2 = {

    tooltip: {
        trigger: 'axis'
    },
    legend: {

        data:['PCT专利申请量','增速'],
        textStyle:{ color:'#fff'}
    },
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },

    xAxis: {
        type: 'category',
        boundaryGap: true,
        data: ['2010','2011','2012','2013','2014','2015','2016'],

         axisLabel: {
                textStyle: {
                    color: '#637c9a'
                }
            },
            splitLine:{show:true , lineStyle:{color:'#0a2239',opacity:1 , type:'dashed'}  }
    },
   yAxis:[  {
       name:'(个)',
        type: 'value', position: 'left',
             axisLabel: {
                textStyle: {
                    color: '#637c9a'
                }
            },

        splitLine:{show:false},
        axisLine:{ lineStyle:{color:'#637c99'}  },
    },
     {
        name:'(%)',
        type: 'value',
          min: -15.0,
         max:50.0,
        position:'right',
             axisLabel: {
                textStyle: {
                    color: '#637c9a'
                },
                   formatter: '{value} %'
            },
            splitNumber: 2,
            splitLine:{show:false}  ,
            axisLine:{ lineStyle:{color:'#637c99'}  },
    },
    ],
    series: [
        {
            name:'PCT专利申请量',
            type:'bar',
            symbol:'circle',
            symbolSize:8,
            barWidth:20,
            itemStyle:{ normal:{ color:'#32c0ac',borderColor:'#32c0ac'} },
            lineStyle: { normal: {color: "#32c0ac"  }},
            data:[0,847,1024,886,1038,1060,1560]
        },
        {
            name:'增速',
            type:'line',
            symbol:'circle',
            yAxisIndex:1,
            xAxisIndex: 0,
            symbolSize:8,
             itemStyle:{
            normal:{ color:'#108dda',borderColor:'#108dda'},  opacity:0},
             lineStyle: { normal: {color: "#108dda"  }
         },

            data:[0,15.2,20.9,-13.5,17.2,2.1,47.2]
        },

    ]
};
var c2_option3 =  {

    tooltip: {
        trigger: 'axis'
    },

    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },

    xAxis: {
        type: 'category',
        boundaryGap: false,
        data: ['2010','2011','2012','2013','2014','2015','2016'],

         axisLabel: {
                textStyle: {
                    color: '#637c9a'
                }
            },
            splitLine:{show:true , lineStyle:{color:'#0a2239',opacity:1 , type:'dashed'}  }
    },
   yAxis:[  {
       min:300,
       name:'(家)',
        type: 'value', position: 'left',
             axisLabel: {
                textStyle: {
                    color: '#637c9a'
                }
            },

        splitLine:{show:false},
        axisLine:{ lineStyle:{color:'#637c99'}  },
    }
    ],
    series: [
        {
           name:'上海外资研发中心数量增长',
            type:'line',
            symbol:'circle',
            symbolSize:8,
            itemStyle:{ normal:{ color:'#32c0ac',borderColor:'#32c0ac'} },
            lineStyle: { normal: {color: "#32c0ac"  }},
            data:[319,334,351,366,381,396,411]
        }


    ]
};

var c3_option1= {

    tooltip: {
        trigger: 'axis'
    },

    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },

    xAxis: {
        type: 'category',
        boundaryGap: false,
        data: ['2010','2011','2012','2013','2014','2015','2016'],

         axisLabel: {
                textStyle: {
                    color: '#637c9a'
                }
            },
            splitLine:{show:true , lineStyle:{color:'#0a2239',opacity:1 , type:'dashed'}  }
    },
   yAxis:[  {
       name:'(亿)',
        type: 'value', position: 'left',
             axisLabel: {
                textStyle: {
                    color: '#637c9a'
                }
            },

        splitLine:{show:false},
        axisLine:{ lineStyle:{color:'#637c99'}  },
    },
     {
        name:'(%)',
        type: 'value',
          min: 10,
         max:20,
        position:'right',
             axisLabel: {
                textStyle: {
                    color: '#637c9a'
                },
                   formatter: '{value} %'
            },
            splitNumber: 2,
            splitLine:{show:false}  ,
            axisLine:{ lineStyle:{color:'#637c99'}  },
    },
    ],
    series: [
        {
            name:'PCT专利申请量',
            type:'line',
            symbol:'circle',
            symbolSize:8,
              smooth: true,
            itemStyle:{ normal:{ color:'#32c0ac',borderColor:'#32c0ac'} },
            lineStyle: { normal: {color: "#32c0ac"  }},
                    areaStyle: {
                normal: {
                    color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                        offset: 0,
                        color: '#32bfab'
                    }, {
                        offset: 1,
                        color: 'rgba(0,0,0,0)'
                    }]),

                    shadowBlur: 20,
                    opacity:0.1,
                },

            },
            data:[58, 56, 51, 52, 54, 42, 50]
        },
        {
            name:'增速',
            type:'line',
            symbol:'circle',
            symbolSize:8,
              smooth: true,
             itemStyle:{ normal:{ color:'#108dda',borderColor:'#108dda'},  opacity:0},
             lineStyle: { normal: {color: "#108dda"  }
         },
             areaStyle: {
                normal: {
                    color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                        offset: 0,
                        color: '#108dda'
                    }, {
                        offset: 1,
                        color: 'rgba(0,0,0,0)'
                    }]),

                    shadowBlur: 20,
                    opacity:0.1,
                },

            },
            data:[16.3, 14.6, 15.1, 16.1, 16.5, 13.9, 18.3]
        },

    ]
};

var c3_option2 = {

    tooltip: {
        trigger: 'axis'
    },
    legend: {

        data:['基础研究经费总额','基础研究经费占比'],
        textStyle:{ color:'#fff'}
    },
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },

    xAxis: {
        type: 'category',
        boundaryGap: true,
        data: ['2010','2011','2012','2013','2014','2015','2016'],

         axisLabel: {
                textStyle: {
                    color: '#637c9a'
                }
            },
            splitLine:{show:true , lineStyle:{color:'#0a2239',opacity:1 , type:'dashed'}  }
    },
   yAxis:[  {
       name:'(亿)',
        type: 'value', position: 'left',
             axisLabel: {
                textStyle: {
                    color: '#637c9a'
                }
            },

        splitLine:{show:false},
        axisLine:{ lineStyle:{color:'#637c99'}  },
    },
     {
        name:'(%)',
        type: 'value',
          min: 6,
         max:10,
        position:'right',
             axisLabel: {
                textStyle: {
                    color: '#637c9a'
                },
                   formatter: '{value} %'
            },
            splitNumber: 2,
            splitLine:{show:false}  ,
            axisLine:{ lineStyle:{color:'#637c99'}  },
    },
    ],
    series: [
        {
            name:'基础研究经费总额',
            type:'bar',
            symbol:'circle',
            symbolSize:8,
            barWidth:20,
            itemStyle:{ normal:{ color:'#32c0ac',borderColor:'#32c0ac'} },
            lineStyle: { normal: {color: "#32c0ac"  }},
            data:[31.04,37.78,49.16,54.87,61.2,76.95,76.22]
        },
        {
            name:'基础研究经费占比',
            type:'line',
            symbol:'circle',
            yAxisIndex:1,
            xAxisIndex: 0,
            symbolSize:8,
             itemStyle:{
            normal:{ color:'#108dda',borderColor:'#108dda'},  opacity:0},
             lineStyle: { normal: {color: "#108dda"  }
         },

            data:[6.4,6.3,7.2,7.1,7.1,8.2,7.4]
        },

    ]
};
