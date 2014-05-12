/* off-canvas sidebar toggle */

$(document).ready(function() {  
  $('[data-toggle=offcanvas]').click(function() {
    $(this).toggleClass('visible-xs text-center');
    $(this).find('i').toggleClass('icon-chevron-right icon-chevron-left');
    $('.row-offcanvas').toggleClass('active');
    $('#lg-menu').toggleClass('hidden-xs').toggleClass('visible-xs');
    $('#xs-menu').toggleClass('visible-xs').toggleClass('hidden-xs');
    $('#btnShow').toggle();
  });
  $('#filterBtn').click(function() {
    $('#filterSmall').toggle("slide");
  });      
});

//$('#filterSmall').hide(); // hide for all screens first

var deviceWidth = 0;
$(window).bind('resize', function () {
  deviceWidth = $('[data-role="page"]').first().width();
 // deviceHeight = $('[data-role="page"]').first().height()-150;
  if(deviceWidth > 768) {
    $('#prime-sidebar-menu').hide();
    $('#filterSmall').hide();
    var pathname = window.location.pathname.substring(1);
    if (pathname ==  "" || pathname == "group" || pathname == "about" || pathname == "organization" || pathname == "feedback" || pathname == "feedbackProv" || pathname == "contact" || pathname == "freedomofinformation" || pathname == "publicsectorinformation") {
      $('div#sidebar').remove();
      $('div#main').attr('class','column col-sm-12 col-xs-12');
      $('div.box').attr('style','background-color:#e9eaed;');
    }
  }
}).trigger('resize');
/*
$('#filterBtn').click(function() {
  $('#filterSmall').show()
});*/
