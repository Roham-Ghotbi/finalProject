$(document).ready(function(){
    $('.tooltipped').tooltip();
    $('[data-toggle="popover"]').popover();  
    $('.fixed-action-btn').floatingActionButton();
    // $('.action-button').addClass('border_'+$(this).data('color'));
    $('.project-line').addClass("bg_".concat($(this).data('color')));
    $('.project-line').hover(function(){
        console.log($(this).data('color'));
        var x = $(this).data('projectId');
        console.log('.' + x);
        $('.' + x).addClass('grey_shadow');
        $(this).addClass('grey_shadow');
        // how to do dynamic color
        // project['color'] + 'shadow'

        $('#title').html("I'm working on " + $(this).data('projectName'));
    }, function(){
        $(this).removeClass('grey_shadow'); 
        $('.action-button').removeClass('grey_shadow');
        $('#title').html("I'm working on ...");

    });

    $('.action-button').hover(function(){
        $(this).addClass('grey_shadow');
        $('#title').html("I'm working on " + $(this).data('projectName'));
    }, function(){
        $(this).removeClass('grey_shadow'); 
        $('#title').html("I'm working on ...");

    });
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


$(".action-button").on('dblclick', function() {
        // move from list_todo container to list_doing container
        console.log($(this).data('color'));

        // $(this).html("Add To To-Do");
        if ($(this).hasClass("bg_" + $(this).data('color'))) {
        	$(this).removeClass("bg_" + $(this).data('color'));
            $(this).addClass("not_done");
	        $(this).addClass("border_" + $(this).data('color'));
        } else{
        	$(this).removeClass("not_done");
	        $(this).addClass("bg_" + $(this).data('color'));
        }
});

$(".slides").sortable({
    placeholder: 'slide-placeholder',
    axis: "y",
    revert: 150,
    start: function(e, ui){
        
        placeholderHeight = ui.item.outerHeight();
        ui.placeholder.height(placeholderHeight + 15);
        $('<div class="slide-placeholder-animator" data-height="' + placeholderHeight + '"></div>').insertAfter(ui.placeholder);
    
    },
    change: function(event, ui) {
        
        ui.placeholder.stop().height(0).animate({
            height: ui.item.outerHeight() + 15
        }, 300);
        
        placeholderAnimatorHeight = parseInt($(".slide-placeholder-animator").attr("data-height"));
        
        $(".slide-placeholder-animator").stop().height(placeholderAnimatorHeight + 15).animate({
            height: 0
        }, 300, function() {
            $(this).remove();
            placeholderHeight = ui.item.outerHeight();
            $('<div class="slide-placeholder-animator" data-height="' + placeholderHeight + '"></div>').insertAfter(ui.placeholder);
        });
        
    },
    stop: function(e, ui) {
        
        $(".slide-placeholder-animator").remove();
        
    },
});