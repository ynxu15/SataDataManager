var c9_items = [
{date:'2017年5月',name:'科技覆约保',amount:5900,count: 16},
{date:'2017年5月',name:'小巨人信用贷',amount:1380,count: 3},
{date:'2017年5月',name:'科技微贷通',amount:400,count: 2},
{date:'2017年5月',name:'创投贷',amount:300,count: 1},

{date:'2016年5月',name:'科技覆约保',amount:12700,count: 34},
{date:'2016年5月',name:'小巨人信用贷',amount:1316,count: 3},
{date:'2016年5月',name:'科技微贷通',amount:400,count: 3},
{date:'2016年5月',name:'创投贷',amount:2050,count: 3},

{date:'2017年1-5月累计',name:'科技覆约保',amount:52530,count: 139},
{date:'2017年1-5月累计',name:'小巨人信用贷',amount:5680,count: 11},
{date:'2017年1-5月累计',name:'科技微贷通',amount:850,count: 6},
{date:'2017年1-5月累计',name:'创投贷',amount:2100,count: 4},

{date:'历年累计',name:'科技覆约保',amount:620556,count: 1832},
{date:'历年累计',name:'小巨人信用贷',amount:263138,count: 399},
{date:'历年累计',name:'科技微贷通',amount:14165,count: 106},
{date:'历年累计',name:'创投贷',amount:19850,count: 27},
{date:'历年累计',name:'其它',amount:64110,count: 47},
];
var c9_cur_date  ='2017年5月';
$(function(){

    c9_cur_date =$('#c9_select').val();

    setc9data();

    $('.ultraSelect').click(function(){

       // $('#c9_select') .click();

    });
    $('#c9_select').change(function(){
       c9_cur_date =$(this).val();
       setc9data();
    });


});

function setc9data()
{
   // var date_arr = c9_cur_date.split(".");
   // var year = date_arr[0];
   // var month = date_arr[1];
    var html = '<h6>'+c9_cur_date+'月科技贷款完成情况统计表</h6>';
    html+= '<table><tr> <th>科技信贷产品</th> <th>贷款额（万元）</th><th>贷款家数</th>  </tr>';
    var total_amount = 0;
    var total_count = 0;
    var j = 0;
    for(var i =0 ;i< c9_items.length ;i++)
    {
         var cur = c9_items[i];

         if(cur.date  && cur.date == c9_cur_date)
         {
           if(j< 4){
                html +='<tr>';
                html+= '<td><p>'+cur.name+'</p></td>';
                html+= '<td><p>'+cur.amount+'</p></td>';
                html+= '<td><p>'+cur.count+'</p></td>';
                html+= '</tr>';
                j++;
             }
           total_amount += cur.amount;
           total_count += cur.count;
         }

    }
    html +='<tr>';
    html+= '<td><p>合计（含其它）</p></td>';
    html+= '<td><p>'+total_amount+'</p></td>';
    html+= '<td><p>'+total_count+'</p></td>';
    html+= '</tr>';
    html+='</table>';
    html+= '<p class="tabP">注：历年累计合辑中包含成果转化信用贷 64110.00万元 47笔 贷款数据</p>';
    $('#c9').html(html);
}


//************第八张图第2页************
var c8_data2 = [
    {date:'2017.06',name:'科技覆约保',amount:5900,count: 16},
    {date:'2017.06',name:'小巨人信用贷',amount:13000,count: 3},
    {date:'2017.06',name:'科技微贷通',amount:400,count: 2},
    {date:'2017.06',name:'创投资贷',amount:300,count: 1},

    {date:'2017.07',name:'科技覆约保',amount:5200,count: 16},
    {date:'2017.07',name:'小巨人信用贷',amount:19000,count: 3},
    {date:'2017.07',name:'科技微贷通',amount:600,count: 2},
    {date:'2017.07',name:'创投资贷',amount:400,count: 1},
];

function setc8_data2()
{
    var html = '<table class="tftable" border="1"><tr><th colspan="3" class="first"><span style="margin-left: -10px">类别</span><span  style="margin-left: 180px">年份</span></th><th>2012</th><th>2013</th><th>2014</th><th>2015</th><th>2016</th></tr><tr class="counts"><td colspan="3">技术合同年度认定数量(项)</td><td>27998</td><td>26297</td><td>25238</td><td>22513</td><td>21203</td></tr><tr class="money"><td colspan="3" >成交金额(亿元)</td><td>588.52</td><td>620.87</td><td>667.99</td><td>707.99</td><td>822.86</td></tr><tr class="counts"><td rowspan="8" class="title" style="width: 30px">其中</td><td class="title" rowspan="2">技术开发</td><td>认定数量(项)</td><td>10974</td><td>10057</td><td>10187</td><td>9579</td><td>9141</td></tr><tr class="money"><td>成交金额(亿元)</td><td>297.14</td><td>267.33</td><td>299.83</td><td>321.49</td><td>309.39</td></tr><tr class="counts"><td rowspan="2" class="title">技术转让</td><td>认定数量(项)</td><td>1170</td><td>1102</td><td>1201</td><td>1050</td><td>1041</td></tr><tr class="money"><td>成交金额(亿元)</td><td>223.48</td><td>230.15</td><td>221.99</td><td>296.98</td><td>338.00</td></tr><tr class="counts"><td rowspan="2" class="title">技术咨询</td><td>认定数量(项)</td><td>3026</td><td>3094</td><td>2876</td><td>2458</td><td>2211</td></tr><tr class="money"><td>成交金额(亿元)</td><td>5.17</td><td>7.40</td><td>5.96</td><td>5.32</td><td>9.69</td></tr><tr class="counts"><td rowspan="2" class="title">技术服务</td><td>认定数量(项)</td><td>12828</td><td>12044</td><td>10974</td><td>9426</td><td>8810</td></tr><tr class="money"><td>成交金额(亿元)</td><td>62.73</td><td>115.99</td><td>140.21</td><td>84.20</td><td>165.78</td></tr></table>';
    $('#c8_table').html(html);
}