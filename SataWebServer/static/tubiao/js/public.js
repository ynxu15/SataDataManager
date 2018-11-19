// JavaScript Document
$(document).ready(function(e) {
	//选项卡
	var tab01 = $('.tab01'),
		content01 = $('.content01');
	tab01.find('li').on('click',function(){
		tab01.find('li').removeClass('cur');
		$(this).addClass('cur');
		content01.hide();
		content01.eq($(this).index()).show();
	});
});
