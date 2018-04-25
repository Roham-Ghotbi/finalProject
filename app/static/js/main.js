$(document).ready(function(){
    $('.modal').modal();
    $('.tooltipped').tooltip();
    $('[data-toggle="popover"]').popover();  
    initializeColors()
    $('.fixed-action-btn').floatingActionButton();
    $('.project-line').focusin(function(){
        var projectName = $(this).data('projectName');
        var action_buttons = $('.action-button');

        // take care of popovers
        $(this).popover('show');
        $(this).data('trigger','none');
        for (var i = action_buttons.length - 1; i >= 0; i--) {
            if ($(action_buttons[i]).data('projectName')===projectName) {
                
                // open every popover
                $(action_buttons[i]).popover('show')
                // disable any accidental triggering 
                $(action_buttons[i]).data('trigger','none');
            }
        }
        console.log($('.btn-floating').data('target'));
        $('.btn-floating').attr('data-target',"actionModal");
        $('.btn-floating').attr('data-tooltip',"Create Action");
        console.log($('.btn-floating').data('target'));
        
        // highlighting
        var x = $(this).data('projectId');
        var color = $(this).data('color');
        var y = color + "_shadow";
        // action button colors
        $('.' + x).addClass(y);
        $(this).addClass(y);

        // fix title
        $(this).attr('data-prev-title',$('#title').html());
        $('#title').html("<font color=" + $(this).data('color') + ">" + $(this).data('projectName')+"</font>");

        // unbind hover functionality
        $(this).unbind('mouseenter mouseleave');
    });
    $('.project-line').focusout(function(){
        var projectName = $(this).data('projectName');
        var action_buttons = $('.action-button');

        // take care of popovers
        $(this).popover('hide');
        for (var i = action_buttons.length - 1; i >= 0; i--) {
            if ($(action_buttons[i]).data('projectName')===projectName) {
                
                // close every popover
                $(action_buttons[i]).popover('hide')
                // enable regular triggering 
                $(action_buttons[i]).data('trigger','hover');
            }   
        }
        console.log($('.btn-floating').data('target'));
        $('.btn-floating').attr('data-target','projectModal');
        $('.btn-floating').attr('data-tooltip',"Create Project");
        console.log($('.btn-floating').data('target'));
        var x = $(this).data('projectId');
        var color = $(this).data('color');
        var y = color + "_shadow";
        // action button colors
        $('.' + x).removeClass(y);
        $(this).removeClass(y);


        // fix title
        $('#title').html($(this).data('prevTitle'));

        // rebind hover functionality
        $(this).hover(function(){
            var x = $(this).data('projectId');
            var color = $(this).data('color');
            var y = color + "_shadow";
            // action button colors
            $('.' + x).addClass(y);
            $(this).addClass(y);
            // how to do dynamic color
            // project['color'] + 'shadow'
            $(this).popover("show");
            $(this).attr('data-prev-title',$('#title').html());
            $('#title').html("I'm working on " + "<font color=" + $(this).data('color') + ">" + $(this).data('projectName')+"</font>");
        }, function(){
            var x = $(this).data('projectId');
            var color = $(this).data('color');
            var y = color + "_shadow";
            // action button colors
            $('.' + x).removeClass(y);
            $(this).removeClass(y);
            $('#title').html($(this).data('prevTitle'));
            $(this).popover("hide");

        });
    });
//     $(".btn-primary").on("click", function () {
//     $('#testButton').attr('data-target','#testModal2');
// });


    $('.project-line').hover(function(){
        var x = $(this).data('projectId');
        var color = $(this).data('color');
        var y = color + "_shadow";
        // action button colors
        $('.' + x).addClass(y);
        $(this).addClass(y);

        $(this).attr('data-prev-title',$('#title').html());
        $('#title').html("I'm working on " + "<font color=" + $(this).data('color') + ">" + $(this).data('projectName')+"</font>");
    }, function(){
        var x = $(this).data('projectId');
        var color = $(this).data('color');
        var y = color + "_shadow";
        // action button colors
        $('.' + x).removeClass(y);
        $(this).removeClass(y);
        $('#title').html($(this).data('prevTitle'));

    });

    $('.action-button').hover(function(){

        var color = $(this).data('color');
        var y = color + "_shadow";
        $(this).addClass(y);
        $('#title').html("I'm working on " + $(this).data('projectName'));
    }, function(){
        var color = $(this).data('color');
        var y = color + "_shadow";
        $(this).removeClass(y);
        $('#title').html("I'm working on ...");

    });
  });
function initializeColors(){
    var project_lines = $('.project-line');
    for (var i = project_lines.length - 1; i >= 0; i--) {
        var x = percentage($(project_lines[i]).data('projectName'));
        console.log(x);
        $(project_lines[i]).attr('data-content',"<font color=" + $(project_lines[i]).data('color') + ">" + x +"</font>");

        var x = 'bg_'+$(project_lines[i]).data('color');
        $(project_lines[i]).addClass(x);
    }
    var action_buttons = $('.action-button')
    for (var i = action_buttons.length - 1; i >= 0; i--) {
        var x = 'border_'+$(action_buttons[i]).data('color');
        if ($(action_buttons[i]).hasClass('done')) {
            $(action_buttons[i]).addClass("bg_" + $(action_buttons[i]).data('color'));
        }
        $(action_buttons[i]).addClass(x);
    }
}
function percentage(projectName) {
    var action_buttons = $('.action-button');

    var done = 0
    var total = 0;
    for (var i = action_buttons.length - 1; i >= 0; i--) {
        if ($(action_buttons[i]).data('projectName') === projectName) {
            total++;
            if ($(action_buttons[i]).hasClass("done")) {
                done++;
            }
        }
    }
    if (total==1) {
        return "0%"
    } else{
        // if impplmenting create action like this, need to keep -1
        return String(parseInt(100*((done-1)/(total-1)))) + "%";   
    }
}

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
        var actionId = $(this).data('actionId');

        // Not Done
        if ($(this).hasClass("bg_" + $(this).data('color'))) {
        	$(this).removeClass("bg_" + $(this).data('color'));
            $(this).removeClass("done");
            $(this).addClass("not_done");
	        $(this).addClass("border_" + $(this).data('color'));
            $.ajax({
              type: "POST",
              url: "./toggle_not_done",
              data: {'action_id': actionId}
            });
        // Done
        } else{
        	$(this).removeClass("not_done");
            $(this).addClass("done");
	        $(this).addClass("bg_" + $(this).data('color'));
            $.ajax({
              type: "POST",
              url: "./toggle_done",
              data: {'action_id': actionId}
            });
        }
        var x = percentage($(this).data('projectName'));
        var sel = ".project-line[data-project-name= '" + $(this).data('projectName') + "']";
        console.log(sel);
        $(sel).attr('data-content',"<font color=" + $(this).data('color') + ">" + x +"</font>");
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