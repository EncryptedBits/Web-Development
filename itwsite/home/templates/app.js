var main = function() {
			
    $(".dropdown").hover(function() {
                $('.dropdown-menu').stop( true, true ).fadeIn("fast");
                $(this).toggleClass('open');
                $('b').toggleClass("caret caret-up");                
            },
            function() {
                $('.dropdown-menu').stop( true, true ).fadeOut("slow");
                $(this).toggleClass('open');
                $('b').toggleClass("caret caret-up");                
            
    });
	
	$(document).scroll(function () {
        var y = $(this).scrollTop();
        var x = $("#nav").position();
        if (y > x.top) {
          $('#nav').addClass('sticky');
		  $('#hlist').addClass('hlistStick');
        } else {
            $('#nav').removeClass('sticky');
			$('#hlist').removeClass('hlistStick');
        }
		
        });
		
		
	$('#respon').click(function(){
		var x = document.getElementById("myTopnav");
			if (x.className === "menu") {
				x.className += " responsive";
			} else {
				x.className = "menu";
			}
		
	});
	
	$(".compBtn").click(function(){
		var a = $(this).attr("id");
		$("#complaintType").text(a);
		$("#complModal").modal();
	});
	
	$("#loginBtn").click(function(){
		var a = $('#usrname').val();
		$("#userid").text(a);
		$('#login').addClass('hide');
		$('#user').addClass('show');
		$('#login').removeClass('show');
		$('#user').removeClass('hide');
	});
	
	$("#myBtn").click(function(){
		$("#myModal").modal();
	});
  
	$('.carousel').carousel({
		interval: 1500
	});
  
};

$(document).ready(main);