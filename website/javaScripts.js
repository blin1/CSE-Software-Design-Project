$(window).load(function(){
	$("[data-toggle]").click(function() {
		var toggle_el = $(this).data("toggle");
		$(toggle_el).toggleClass("open-sidebar");
	});
	$(".swipe-area").swipe({
		swipeStatus:function(event, phase, direction, distance, duration, fingers){
			if (phase=="move" && direction=="right") {
				$(".container").addClass("open-sidebar");
				return false;
			}
			if (phase=="move" && direction=="left") {
				$(".container").removeClass("open-sidebar");
				return false;
			}
		}
	}); 
});

function hideA(x) {
	if (x.checked) {
		document.getElementById("A").style.visibility="hidden";
		document.getElementById("B").style.visibility="visible";    
	}
}

function hideB(x) {
    if (x.checked) {
    	document.getElementById("B").style.visibility="hidden";
    	document.getElementById("A").style.visibility="visible";
    }
}

