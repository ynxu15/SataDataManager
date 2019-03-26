
function setChart1(){
	// 基于准备好的dom，初始化echarts实例
     var myChart = echarts.init(document.getElementById('chart1'));
	
	var	option = {
		//backgroundColor: '#ccc',	// 背景颜色
	    title: {                    // 图表标题
	        text: "企业营收影响因子分析",           // 标题文本
	        left : '3%',                    // 标题距离左侧边距
	        top : '3%',                     // 标题距顶部边距
			textStyle : {                       // 标题样式
				color : '#000',                     // 标题字体颜色
				fontSize : '20',                    // 标题字体大小
			}
	    },
//	    tooltip: {                  // 提示框的配置
//	        formatter: function(param) {
//	            if (param.dataType === 'edge') {
//	                //return param.data.category + ': ' + param.data.target;
//	                return param.data.target;
//	            }
//	            //return param.data.category + ': ' + param.data.name;
//	            return param.data.name;
//	        }
//	    },
	    
	    series: [{
	        type: "graph",          // 系列类型:关系图
	        top: '10%',             // 图表距离容器顶部的距离
	        roam: true,             // 是否开启鼠标缩放和平移漫游。默认不开启。如果只想要开启缩放或者平移，可以设置成 'scale' 或者 'move'。设置成 true 为都开启
	        focusNodeAdjacency: true,   // 是否在鼠标移到节点上的时候突出显示节点以及节点的边和邻接节点。[ default: false ]
	                force: {                // 力引导布局相关的配置项，力引导布局是模拟弹簧电荷模型在每两个节点之间添加一个斥力，每条边的两个节点之间添加一个引力，每次迭代节点会在各个斥力和引力的作用下移动位置，多次迭代后节点会静止在一个受力平衡的位置，达到整个模型的能量最小化。
	                                // 力引导布局的结果有良好的对称性和局部聚合性，也比较美观。
	            repulsion: 1000,            // [ default: 50 ]节点之间的斥力因子(关系对象之间的距离)。支持设置成数组表达斥力的范围，此时不同大小的值会线性映射到不同的斥力。值越大则斥力越大
	            //edgeLength: [150, 100]      // [ default: 30 ]边的两个节点之间的距离(关系对象连接线两端对象的距离,会根据关系对象值得大小来判断距离的大小)，
	                                        // 这个距离也会受 repulsion。支持设置成数组表达边长的范围，此时不同大小的值会线性映射到不同的长度。值越小则长度越长。如下示例:
	                                        // 值最大的边长度会趋向于 10，值最小的边长度会趋向于 50      edgeLength: [10, 50]
	        },
	        layout: "force",            // 图的布局。[ default: 'none' ]
	                                    // 'none' 不采用任何布局，使用节点中提供的 x， y 作为节点的位置。
	                                    // 'circular' 采用环形布局;'force' 采用力引导布局.
	        // 标记的图形
	        symbol: 'circle',
	        lineStyle: {            // 关系边的公用线条样式。其中 lineStyle.color 支持设置为'source'或者'target'特殊值，此时边会自动取源节点或目标节点的颜色作为自己的颜色。
	            normal: {
	                color: '#000',          // 线的颜色[ default: '#aaa' ]
	                width: 1,               // 线宽[ default: 1 ]
	                type: 'solid',          // 线的类型[ default: solid ]   'dashed'    'dotted'
	                opacity: 0.5,           // 图形透明度。支持从 0 到 1 的数字，为 0 时不绘制该图形。[ default: 0.5 ]
	                curveness: 0            
	            }
	        },
	        label: {                // 关系对象上的标签
	            normal: {
	                show: true,                 // 是否显示标签
	                position: "inside",         // 标签位置:'top''left''right''bottom''inside''insideLeft''insideRight''insideTop''insideBottom''insideTopLeft''insideBottomLeft''insideTopRight''insideBottomRight'
	                textStyle: {                // 文本样式
	                    fontSize: 16
	                }
	            }
	        },
	        edgeLabel: {                // 连接两个关系对象的线上的标签
	            normal: {
	                show: true,
	                textStyle: {                
	                    fontSize: 14
	                },
	                formatter: function(param) {        // 标签内容
	                    return param.data.category;
	                }
	            }
	        },
	        data: [{
	            name: "公司营收",
	            draggable: true,                // 节点是否可拖拽，只在使用力引导布局的时候有用。
	            symbolSize: [100, 100],         // 关系图节点标记的大小，可以设置成诸如 10 这样单一的数字，也可以用数组分开表示宽和高，例如 [20, 10] 表示标记宽为20，高为10。
	            itemStyle: {
	            	color: '#666666'				// 关系图节点标记的颜色
	            },
	            category: "收入支出分析"         // 数据项所在类目的 index。
	        }, {
	            name: "企业经营",
	            draggable: true,
	            symbolSize: [80, 80],
	            itemStyle: {
	            	color: '#990033'
	            },
	            category: "收入+"
	        }, {
	            name: "政府扶持",
	            draggable: true,
	            symbolSize: [80, 80],
	            itemStyle: {
	            	color: '#006633'
	            },
	            category: "支出-"
	        }, {
	            name: "经济发展",
	            draggable: true,
	            symbolSize: [80, 80],
	            itemStyle: {
	            	color: '#cccc00'
	            },
	            category: "支出-"
	        }, {
	            name: "生产成本",
	            draggable: true,
	            symbolSize: [50, 50],
	            itemStyle: {
	            	color: '#cc0044'
	            },
	            category: "企业经营-"
	        }, {
	            name: "债务",
	            draggable: true,
	            symbolSize: [50, 50],
	            itemStyle: {
	            	color: '#cc0044'
	            },
	            category: "企业经营-"
	        }, {
	            name: "创新",
	            draggable: true,
	            symbolSize: [50, 50],
	            itemStyle: {
	            	color: '#cc0044'
	            },
	            category: "企业经营-"
	        }, {
	            name: "公司策略",
	            draggable: true,
	            symbolSize: [50, 50],
	            itemStyle: {
	            	color: '#cc0044'
	            },
	            category: "企业经营-"
	        }, {
	            name: "人才",
	            draggable: true,
	            symbolSize: [50, 50],
	            itemStyle: {
	            	color: '#cc0044'
	            },
	            category: "企业经营-"
	        }, {
	            name: "高新企业评定",
	            draggable: true,
	            symbolSize: [50, 50],
	            itemStyle: {
	            	color: '#009933'
	            },
	            category: "政府扶持-"
	        }, {
	            name: "项目合作",
	            draggable: true,
	            symbolSize: [50, 50],
	            itemStyle: {
	            	color: '#009933'
	            },
	            category: "政府扶持-"
	        }, {
	            name: "税收减免",
	            draggable: true,
	            symbolSize: [50, 50],
	            itemStyle: {
	            	color: '#009933'
	            },
	            category: "政府扶持-"
	        }],
//	        categories: [{              // 节点分类的类目，可选。如果节点有分类的话可以通过 data[i].category 指定每个节点的类目，类目的样式会被应用到节点样式上。图例也可以基于categories名字展现和筛选。
//	            name: "收入支出分析"            // 类目名称，用于和 legend 对应以及格式化 tooltip 的内容。
//	        }, {
//	            name: "收入+"
//	        }, {
//	            name: "支出-"
//	        }, {
//	            name: "支出-"
//	        }, {
//	            name: "剩余="
//	        }],
	        links: [{                   // 节点间的关系数据
	            target: "企业经营",
	            source: "公司营收",
	            category: "0.6",              // 关系对象连接线上的标签内容
	        }, {
	            target: "政府扶持",
	            source: "公司营收",
	            category: "0.2"
	        }, {
	            target: "经济发展",
	            source: "公司营收",
	            category: "0.2"
	        }, {
	            target: "生产成本",
	            source: "企业经营",
	            category: "0.06"
	        }, {
	            target: "债务",
	            source: "企业经营",
	            category: "0.05"
	        }, {
	            target: "创新",
	            source: "企业经营",
	            category: "0.1"
	        }, {
	            target: "公司策略",
	            source: "企业经营",
	            category: "0.3"
	        }, {
	            target: "人才",
	            source: "企业经营",
	            category: "0.09"
	        }, {
	            target: "高新企业评定",
	            source: "政府扶持",
	            category: "0.03"
	        }, {
	            target: "项目合作",
	            source: "政府扶持",
	            category: "0.08"
	        }, {
	            target: "税收减免",
	            source: "政府扶持",
	            category: "0.09"
	        }]
	    }],
	    
	    animationEasingUpdate: "quinticInOut",          // 数据更新动画的缓动效果。[ default: cubicOut ]    "quinticInOut"
	    animationDurationUpdate: 100                    // 数据更新动画的时长。[ default: 300 ]
	};
	
	// 使用刚指定的配置项和数据显示图表
	myChart.setOption(option)
}


$(function(){
	setChart1();
//	setChart2();
//	setChart3(); 
//	setChart4();
//	setChart5();
//  setChart6();
});

	