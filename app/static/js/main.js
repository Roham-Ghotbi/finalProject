$(document).ready(function(){
        $('[data-toggle="popover"]').popover();   
      });
      $(".pop").popover({ trigger: "manual" , html: true, animation:false})
            .on("mouseenter", function () {
                var _this = this;
                $(this).popover("show");
                $(".popover").on("mouseleave", function () {
                    $(_this).popover('hide');
                });
            }).on("mouseleave", function () {
                var _this = this;
                setTimeout(function () {
                    if (!$(".popover:hover").length) {
                        $(_this).popover("hide");
                    }
                }, 0);
        });


$(".action-button").on('click', function() {
        // move from list_todo container to list_doing container
        console.log("I'm in action-button");

        // $(this).html("Add To To-Do");
        if ($(this).hasClass("done")) {
        	$(this).removeClass("done");
	        $(this).addClass("not_done");
        } else{
        	$(this).removeClass("not_done");
	        $(this).addClass("done");
        }
});