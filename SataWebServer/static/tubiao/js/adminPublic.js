$(function(){
	//aside自动高度
	var aside = $('#aside');
	aside.height(window.innerHeight);
	$(window).resize(function(){
		aside.height(window.innerHeight);
	});
	
	// 侧边导航动效
	var asideNav = $('.asideNav');
	asideNav.find('li').on('click',function(){
		asideNav.find('li').removeClass('cur').addClass('down');
		$(this).css({
			background : '#0d2b4d',
			color : '#a3b8cd'
		}).addClass('cur');
		/*
		$(this).children('span:nth-child(1)').css({
			backgroundImage : 'url(static/images/admin/navIconUp.png)'
		});
		*/
		$(this).find('span:nth-child(3)').css({
			backgroundPosition : '-9px 0',
		});
		$(this).find('div.asideNavMore').show();
	});

	
	var asideNavMore = $('.asideNavMore')
	asideNavMore.find('p').on('click',function(){
		asideNavMore.find('p').removeClass('cur').addClass('down');
		$(this).css({
			borderRight : '#207dda 4px solid',
			color : '#207dda'
		}).addClass('cur');
		
//		$(this).find('span:nth-child(1)').css({
//			backgroundImage : 'url(static/images/admin/navIconUp.png)'
//		});
		$(this).find('div.asideNavMore').show();
	});
	if(asideNav.find('p').hasClass('cur')){
		//$(this).find('p').
	}
	
});

// JavaScript Document
var btnStatus = $('.adminStatus');
btnStatus.on('click',function(e){
	if(btnStatus.hasClass('on')){
		
	} else {
		$(this).addClass('on');
		if($('.adminMore').is(':hidden')){
			$('.adminMore').show();
			$(this).css({
				background : '#040e1a',
				color : '#7d98b2',
				borderColor : '#e6e6e6'
			});
		} else {
			$('.adminMore').hide()
		}
		$(document).on("click", function(){
			$(".adminMore").hide();
			btnStatus.css({
				background : '#fff',
				color : '#7d98b2',
				borderColor : '#e6e6e6'
			}).find('span:nth-child(3)').css('background-position','-9px 0');
			btnStatus.removeClass('on');
			e.stopPropagation();
		});
	}
});
$('.adminStatus').on("click", function(e){
	e.stopPropagation();
});
