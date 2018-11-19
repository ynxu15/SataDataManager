//自定义checkbox 多选
var multipleCheck = $('.multipleCheck');
multipleCheck.on('click',function(){
	if($(this).find('span.checkBox').hasClass('checked')){
		$(this).find('span.checkBox').removeClass('checked');
	} else {
		$(this).find('span.checkBox').addClass('checked');
	}
});

//自定义checkbox 单选
var singleCheck = $('.singleCheck');
singleCheck.on('click',function(){
	singleCheck.find('span.checkBox').removeClass('checked');
	$(this).find('span.checkBox').addClass('checked');
});

var singleCheck2 = $('.singleCheck2');
singleCheck2.on('click',function(){
	singleCheck2.find('span.checkBox').removeClass('checked');
	$(this).find('span.checkBox').addClass('checked');
});

var singleCheck3 = $('.singleCheck3');
singleCheck3.on('click',function(){
	singleCheck3.find('span.checkBox').removeClass('checked');
	$(this).find('span.checkBox').addClass('checked');
});


//input焦点动效
var inp01 = $('.inp01');
inp01.on('focus',function(){
	inp01.removeClass('borderBlue01').addClass('borderGray01');
	$(this).addClass('borderBlue01').removeClass('borderGray01');
});
inp01.on('blur',function(){
	inp01.removeClass('borderBlue01').addClass('borderGray01');
});

//选项卡
var tab01 = $('.tab01'),
	content01 = $('.content01');
tab01.find('li').on('click',function(){
	tab01.find('li').removeClass('pWhite bgBlue01 borderBlue01').addClass('borderGray01 bgWhite');
	$(this).addClass('pWhite borderBlue01 bgBlue01').removeClass('bgWhite');
	content01.hide();
	content01.eq($(this).index()).show();
	//alert($(this).index());
});

//分页
var pager01 = $('.pager01');
pager01.find('li').on('click',function(){
	if($(this).index() != 0 && $(this).index() != pager01.find('li').length -1){
		pager01.find('li').removeClass('cur');
		$(this).addClass('cur');
	}
});