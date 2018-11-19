var c1_chart, c2_chart,c3_chart,c7_chart,c8_chart,c8_table;

var c1_cur = 1,c2_cur =1 ,c3_cur=1,c7_cur =1,c8_cur=1;
$(function(){
    c1_chart = echarts.init(document.getElementById('c1'));
    c2_chart = echarts.init(document.getElementById('c2'));
    c3_chart = echarts.init(document.getElementById('c3'));


   var c4_chart = echarts.init(document.getElementById('c4'));
   c4_chart.setOption(c4_option);

   var c5_chart = echarts.init(document.getElementById('c5'));
   c5_chart.setOption(c5_option);

   var c6_chart = echarts.init(document.getElementById('c6'));
   c6_chart.setOption(c6_option);

    c7_chart = echarts.init(document.getElementById('c7'));
    c8_chart = echarts.init(document.getElementById('c8'));
    c8_table=$('#c8_table');

   set_c1_chart();
   set_c2_chart();
   set_c3_chart();
   set_c7_chart();
   set_c8_chart();
   $('.validMore img').click(function(){
       var idx=   $(this).attr('id');
       var num = Number(idx.replace(/[^0-9]/ig,""));
       var act  = idx.split("_")[2];

       switch(num)
       {
          case 1:
            c1_cur = sw_num(c1_cur,3,act);
             set_c1_chart();
          break;
          case 2:
            c2_cur = sw_num(c2_cur,3,act);
            set_c2_chart();
          break;
          case 3:
            c3_cur = sw_num(c3_cur,2,act);
            set_c3_chart();
          break;
          case 7:
          c7_cur = sw_num(c7_cur,3,act);
          set_c7_chart();
           break;
          case 8:
          c8_cur = sw_num(c8_cur,3,act);
          set_c8_chart();
           break;
       }

      });
});
function set_c1_chart()
{
    c1_chart.clear();
    switch(c1_cur)
    {
       case 1:
       $('#c1_title').html('上海R&D支出及其相当于GDP比例年度变化 ');
       c1_chart.setOption(c1_option1);
       break;
       case 2:
       $('#c1_title').html('上海国家级研发机构数量');
       c1_chart.setOption(c1_option2);
       break;
       case 3:
       $('#c1_title').html('上海万人发明专利增长');
       c1_chart.setOption(c1_option3);
       break;
    }

}

function set_c2_chart()
{
    c2_chart.clear();
    switch(c2_cur)
    {
       case 1:
       $('#c2_title').html('上海规上工业企业R&D与主营收入比例 ');
       c2_chart.setOption(c2_option1);
       break;
       case 2:
       $('#c2_title').html('上海PCT专利申请量增长');
       c2_chart.setOption(c2_option2);
       break;
       case 3:
       $('#c2_title').html('上海外资研发中心数量增长');
       c2_chart.setOption(c2_option3);
       break;
    }

}
function set_c3_chart()
{

    c3_chart.clear();
    switch(c3_cur)
    {
       case 1:
       $('#c3_title').html('上海获国家级科技成果奖励数及全国比重');
       c3_chart.setOption(c3_option1);
       break;
       case 2:
       $('#c3_title').html('上海基础研究经费投入');
       c3_chart.setOption(c3_option2);
       break;

    }
}

function set_c7_chart()
{
    c7_chart.clear();
    $('#c7_title').html('创新创业服务 ');
    switch(c7_cur)
    {
       case 1:
       c7_chart.setOption(c7_option1);
       break;
       case 2:
       c7_chart.setOption(c7_option2);
       break;
       case 3:
       c7_chart.setOption(c7_option3);
       break;
    }

}
function set_c8_chart()
{
    c8_chart.clear();
    c8_table.html("");
    switch(c8_cur)
    {
       case 1:
       c8_chart.setOption(c8_option1);
       break;
       case 2:
       setc8_data2();
       break;
       case 3:
       c8_chart.setOption(c8_option3);
       break;

    }
}

function sw_num(cur,max,act)
{
      if(act == 'left')
      {
          cur --;
      }else if(act == 'right')
      {
           cur ++;
      }
      if(cur <1)
      {
          cur = max;
      }
      if(cur > max)
      {
          cur = 1;
      }
      return cur ;
}
