var c7_option1 = {

    tooltip: {
        trigger: 'axis',

    },
    title:{ text:'上海科技企业孵化建设' ,
       left:'35%',
                textStyle:{ color:'#7493c0',align:'right'}
    },
    legend: {
        top:30,
        left:'3%',
        data:[{name:'RD支出'
        //,icon:'image://../static/images/next.png'
      },{name:'相当于GDP'}],
        textStyle:{ color:'#fff'}
    },
    grid: {
        top:90,
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },

    xAxis: {
        type: 'category',
        boundaryGap: true,
        data: ['2012','2013','2014','2015','2016'],

         axisLabel: {
                textStyle: {
                    color: '#637c9a'
                }
            },
              axisTick: {
                alignWithLabel: true,
                show:false
            },
            splitLine:{show:true , lineStyle:{color:'#0a2239',opacity:1 , type:'dashed'}  }
    },
   yAxis:[  {
       name:'(平方米)',
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
        name:'(家)',
        type: 'value',
        min: 50,
        max:200,
        position:'right',
             axisLabel: {
                textStyle: {
                    color: '#637c9a'
                },
                   formatter: '{value}'
            },
            splitNumber: 2,
            splitLine:{show:false}  ,
            axisLine:{ lineStyle:{color:'#637c99'}  },
    },
    ],
    series: [
        {
            name:'场地面积',
            type:'bar',
            symbol:'circle',
            symbolSize:8,
            barWidth:20,

            itemStyle:{ normal:{ color:'#7d503d', opacity:0.6} },
            lineStyle: { normal: {color: "#7d503d"  }},
            data:[1170009, 1378819, 1494599, 1859896, 2118193]
        },
        {
            name:'累计孵化基地数量',
            type:'line',
            symbol:'circle',
            yAxisIndex:1,
            symbolSize:8,
             itemStyle:{ normal:{ color:'#d4a15a',borderColor:'#d4a15a'},  opacity:0},
             lineStyle: { normal: {color: "#d4a15a"  }
         },
            data:[85, 93, 107, 139, 159]
        }
    ]
};



 var c7_option2 = {

    tooltip: {
        trigger: 'axis',

    },
    title:{ text:'在孵企业数及毕业数' ,
        left:'35%',
        textStyle:{ color:'#7493c0',align:'right'}
    },
    legend: {
        top:30,
        left:'38%',
        data:[{name:'在孵企业数'
      },{name:'累计毕业数'}],
        textStyle:{ color:'#fff'}
    },
    grid: {
        top:90,
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },

    xAxis: {
        type: 'category',
        boundaryGap: true,
        data: ['2012','2013','2014','2015','2016' ],

         axisLabel: {
                textStyle: {
                    color: '#637c9a'
                }
            },
              axisTick: {
                alignWithLabel: true,
                show:false
            },
            splitLine:{show:true , lineStyle:{color:'#0a2239',opacity:1 , type:'dashed'}  }
    },
   yAxis:[  {
       name:'(平方米)',
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
        name:'(家)',
        type: 'value',
          min: 0,
         max:3000,
        position:'right',
             axisLabel: {
                textStyle: {
                    color: '#637c9a'
                },
                   formatter: '{value} '
            },
            splitNumber: 3,
            splitLine:{show:false}  ,
            axisLine:{ lineStyle:{color:'#637c99'}  },
    },
    ],
    series: [
        {
            name:'在孵企业数',
            type:'bar',
            symbol:'circle',
            symbolSize:8,
            barWidth:20,

            itemStyle:{ normal:{ color:'#7d503d', opacity:0.6} },
            lineStyle: { normal: {color: "#7d503d"  }},
            data:[3995,4445,4654,5519,6646]
        },
        {
            name:'累计毕业数',
            type:'line',
            symbol:'circle',
            symbolSize:8,
            yAxisIndex:1,
            itemStyle:{ normal:{ color:'#d4a15a',borderColor:'#d4a15a'},  opacity:0},
             lineStyle: { normal: {color: "#d4a15a"  }
         },
            data:[1497,1698,2059,2397,2749]
        },

    ]
};

var c7_option3  = {

    tooltip: {
        trigger: 'axis',

    },
    title:{ text:'就业人数及上缴税金总额' ,
       left:'35%',
                textStyle:{ color:'#7493c0',align:'right'}
    },
    legend: {
        top:30,
        left:'38%',
        data:[{name:'就业人数'

      },{name:'上缴税金总额'}],
        textStyle:{ color:'#fff'}
    },
    grid: {
        top:90,
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },

    xAxis: {
        type: 'category',
        boundaryGap: true,
        data: ['2012','2013','2014','2015','2016' ],

         axisLabel: {
                textStyle: {
                    color: '#637c9a'
                }
            },
              axisTick: {
                alignWithLabel: true,
                show:false
            },
            splitLine:{show:true , lineStyle:{color:'#0a2239',opacity:1 , type:'dashed'}  }
    },
   yAxis:[  {
       name:'(人)',
                 min: 0,
         max:120000,
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
        name:'(万元)',
        type: 'value',
          min: 0,
         max:11000,
        position:'right',
             axisLabel: {
                textStyle: {
                    color: '#637c9a'
                },
                   formatter: '{value} '
            },
            splitNumber: 3,
            splitLine:{show:false}  ,
            axisLine:{ lineStyle:{color:'#637c99'}  },
    },
    ],
    series: [
        {
            name:'就业人数',
            type:'bar',
            symbol:'circle',
            symbolSize:8,
            barWidth:20,

            itemStyle:{ normal:{ color:'#7d503d', opacity:0.6} },
            lineStyle: { normal: {color: "#7d503d"  }},
            data:[59562,69074,60267,70826,100424]
        },
        {
            name:'上缴税金总额',
            type:'line',
            symbol:'circle',
            symbolSize:8,
            yAxisIndex:1,
            itemStyle:{ normal:{ color:'#d4a15a',borderColor:'#d4a15a'},  opacity:0},
             lineStyle: { normal: {color: "#d4a15a"  }
         },
            data:[4581,6947,7345,9311,10100]
        },

    ]
};
 var c8_option1 ={

    tooltip: {
        trigger: 'axis'
    },
   title:{ text:'上海高校院所使用来自企业研发资金' ,
       left:'26%',
                textStyle:{ color:'#7493c0',align:'right'}
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
   yAxis: {
       name:'(亿元)',
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
            name:'研发资金',
            type:'line',
            symbol:'circle',
            symbolSize:8,
            smooth: true,

            itemStyle:{ normal:{ color:'#d8a55b',borderColor:'#d8a55b'} },
            lineStyle: { normal: {color: "#d8a55b"  }},
             areaStyle: {
                normal: {
                    color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                        offset: 0,
                        color: '#d8a55b'
                    }, {
                        offset: 1,
                        color: 'rgba(0,0,0,0)'
                    }]),

                    shadowBlur: 20,
                    opacity:0.2,
                },

            },
            data:[22.07,25.13,23.25,30.49,32.13,32.58,38.26]
        }
    ]
};

var c8_option3 = {

    tooltip: {
        trigger: 'axis'
    },
   title:{ text:'上海向国内外输出技术合同占比' ,
       left:'30%',
                textStyle:{ color:'#7493c0',align:'right'}
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
   yAxis: {
       name:'(亿元)',
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
            type:'line',
            symbol:'circle',
            symbolSize:8,
            smooth: true,

            itemStyle:{ normal:{ color:'#d8a55b',borderColor:'#d8a55b'} },
            lineStyle: { normal: {color: "#d8a55b"  }},
             areaStyle: {
                normal: {
                    color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                        offset: 0,
                        color: '#d8a55b'
                    }, {
                        offset: 1,
                        color: 'rgba(0,0,0,0)'
                    }]),

                    shadowBlur: 20,
                    opacity:0.2,
                },

            },
            data:[22.07,25.13,23.25,30.49,32.13,32.58,38.26]
        }
    ]
};