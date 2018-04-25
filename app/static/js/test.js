$(document).ready(function(){
    $('[data-toggle="<popove></popove>r"]').popover();  
    $("[data-toggle='toggle']").click(function() {
    var selector = $(this).data("target");
    $(selector).toggleClass('in');
    });

    // var hideWidth = '-490px'; //width that will be hidden
    // var collapsibleEl = $('.collapsible'); //collapsible element
    // var buttonEl =  $(".collapsible button"); //button inside element

    // collapsibleEl.css({'margin-left': hideWidth}); //on page load we'll move and hide part of elements
    
    // $(buttonEl).click(function()
    // {
    //     var curwidth = $(this).parent().offset(); //get offset value of the element
    //     if(curwidth.left>0) //compare margin-left value
    //     {
    //         //animate margin-left value to -490px
    //         $(this).parent().animate({marginLeft: hideWidth}, 300 );
    //         $(this).html('&raquo;'); //change text of button
    //     }else{
    //         //animate margin-left value 0px
    //         $(this).parent().animate({marginLeft: "0"}, 300 );  
    //         $(this).html('&laquo;'); //change text of button
    //     }
    // });

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
