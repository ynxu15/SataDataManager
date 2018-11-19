var c4_option = {

    tooltip: {
        trigger: 'axis'
    },
    legend: {
        data:['两项税收减免额','地方财政科技拨款','减免税额与地方财政科技拨款比例'],
        textStyle:{ color:'#fff'}
    },
<!--     grid: {
        left: 12,
        right: 12,
        bottom: 20,
        containLabel: true
    }, -->

    xAxis: {
        type: 'category',

        data: ['2010','2011','2012','2013','2014','2015','2016' ],

         axisLabel: {
                textStyle: {
                    color: '#637c9a'
                }
            },
            axisTick: {
                alignWithLabel: true,
                show:false
            }
    },
   yAxis:[  {
    name:'(亿)',
    nameTextStyle:{color:'#fff' ,align:'left',padding:[0,30,0,0]},
        type: 'value', position: 'left',
             axisLabel: {
                textStyle: {
                    color: '#637c9a'
                }
            },
        splitLine:{show:false},
        axisTick:{show:false}
    },

    {
        name:'(%)',
        type: 'value',
         min: 0,
         max: 100,
        position:'right',

             axisLabel: {
                textStyle: {
                    color: '#fff'
                },
                   formatter: '{value} %'
            },
            splitLine:{show:false}    ,
            axisLine:{ lineStyle:{color:'#637a97'} ,  },
            axisLabel:{color:'#637a97' }, axisTick:{show:false}
    },
    ],
    series: [
        {
            name:'两项税收减免额',
            type:'bar',
            barWidth:4,
            itemStyle:{ normal:{ color:'#815bd8'} },
            data:[118.6,144.0,154.8,173.9,191.9,264.5,259.0]
        },
        {
            name:'地方财政科技拨款',
            type:'bar',
               barWidth:4,
             itemStyle:{ normal:{ color:'#108dda'} },
            data:[202.0,218.5,254.4,257.7,262.3,271.9,341.7]
        },
        {
            name:'减免税额与地方财政科技拨款比例',
            type:'line',
            symbol:'circle',
            symbolSize:3,
            yAxisIndex:1,
            itemStyle:{ normal:{ color:'#815bd8',borderColor:'#32c0ac'} },
            lineStyle: { normal: {color: "#815bd8"  }},
            data:[58.7,65.9,60.9,67.5,73.1,97.3,75.8]
        },

    ]
};

var  c5_option = {

    tooltip: {
        trigger: 'axis'
    },
    legend: {
        data:['享受企业数','研发费加计扣除额','减免所得税额'],
        textStyle:{ color:'#fff'}
    },
    grid: {
        left: 12,
        right: 12,
        bottom: 20,
        containLabel: true
    },

    xAxis: {
        type: 'category',

        data: ['2012','2013','2014','2015','2016'],

         axisLabel: {
                textStyle: {
                    color: '#637c9a'
                }
            },
            axisTick: {
                alignWithLabel: true,
                show:false
            }
    },
   yAxis:[  {
    name:'(亿)',
    nameTextStyle:{color:'#fff' ,align:'left',padding:[0,30,0,0]},
        type: 'value', position: 'left',
             axisLabel: {
                textStyle: {
                    color: '#637c9a'
                }
            },
        splitLine:{show:false},
        axisTick:{show:false}
    },

    {
        name:'(家)',
        type: 'value',
         min: 4000,
         max: 10000,
        position:'right',

             axisLabel: {
                textStyle: {
                    color: '#fff'
                },
                   formatter: '{value} %'
            },
            splitLine:{show:false}    ,
            axisLine:{ lineStyle:{color:'#637a97'} ,  },
            axisLabel:{color:'#637a97' }, axisTick:{show:false}
    },
    ],
    series: [
        {
            name:'享受企业数',
            type:'line',
            symbol:'circle',
            yAxisIndex:1,
            itemStyle:{ normal:{ color:'#32c0ac',borderColor:'#32c0ac'} },
            lineStyle: { normal: {color: "#32c0ac"  }},
            data:[4092,4876,5852,6794,8926]
        },
        {
            name:'研发费加计扣除额',
            type:'bar',
            barWidth:4,
            itemStyle:{ normal:{ color:'#108dda'} },
            data:[234.83,289.58,335.00,407.99,469.69]
        },
        {
            name:'减免所得税额',
            type:'bar',
            symbolSize:8,
            barWidth:4,
            itemStyle:{ normal:{ color:'#815bd8',borderColor:'#815bd8'} },
            lineStyle: { normal: {color: "#815bd8"  }},
            data:[58.70,72.40,83.75,102.00,117.42]
        },

    ]
};



var c6_option  = {

    tooltip: {
        trigger: 'axis'
    },
    legend: {
        data:['全市高企总数','享受企业数','减免税额','全市高企增长率'],
        textStyle:{ color:'#fff'}
    },
    grid: {
        left: 12,
        right: 100,
        bottom: 20,
        containLabel: true
    },

    xAxis: {
        type: 'category',

        data: ['2012','2013','2014','2015','2016'],

         axisLabel: {
                textStyle: {
                    color: '#637c9a'
                }
            },
            axisTick: {
                alignWithLabel: true
            }
    },
   yAxis:[  {
    name:'(家)',
    nameTextStyle:{color:'#fff' ,align:'left',padding:[0,30,0,0]},
        type: 'value', position: 'left',
             axisLabel: {
                textStyle: {
                    color: '#637c9a'
                }
            },
        splitLine:{show:false}
    },
     {
        type: 'value',
          min: 0,
         max: 10,
        position:'right',
             axisLabel: {
                textStyle: {
                    color: '#637c9a'
                },
                   formatter: ''
            },
            axisTick:{show:false},
            splitLine:{show:false}
    },
    {
        name:'(亿)',
        type: 'value',
          min: 0,
         max: 180,
        position:'right',
        offset:50,  //7c353b
             axisLabel: {
                textStyle: {
                    color: 'red'
                },
                   formatter: '{value}'
            },
            splitNumber: 2,
            splitLine:{show:false}   ,
            axisTick:{show:false},
            axisLine:{ lineStyle:{color:'#617792',type:'dashed'} ,  },
            axisLabel:{color:'#617792' }
    }, {
        name:'(%)',
        type: 'value',
          min: 0,
         max: 22,
        position:'right',
        offset:100,
             axisLabel: {
                textStyle: {
                    color: '#fff'
                },
                   formatter: '{value} %'
            },
            splitLine:{show:false}    ,
            axisLine:{ lineStyle:{color:'#7c353b'} ,  },
            axisLabel:{color:'#7c353b' }
    },
    ],
    series: [
        {
            name:'全市高企总数',
            type:'bar',
            barWidth:4,
            yAxisIndex:0,
            itemStyle:{ normal:{ color:'#815bd8'} },
            data:[4311, 5140, 5425, 6071, 6938]
        },
        {
            name:'享受企业数',
            type:'bar',
               barWidth:4,
               yAxisIndex:0,
             itemStyle:{ normal:{ color:'#108dda'} },
            data:[2582,2874,3021,3168,3375]
        },
        {
            name:'减免税额',
            type:'line',
            symbol:'circle',
            symbolSize:3,
            yAxisIndex:2,
            itemStyle:{ normal:{ color:'#32c0ac',borderColor:'#32c0ac'} },
            lineStyle: { normal: {color: "#32c0ac"  }},
            data:[97.62,101.45,108.85,162.53,142.62]
        },
        {
            name:'全市高企增长率',
            type:'line',
            symbol:'circle',
            symbolSize:3,
            yAxisIndex:3,
             itemStyle:{ normal:{ color:'#7c353b',borderColor:'#7c353b'},  opacity:0},
             lineStyle: { normal: {color: "#7c353b"  }
         },
            data:[20.12,19.23,5.54,11.91,14.17]
        },
    ]
};

