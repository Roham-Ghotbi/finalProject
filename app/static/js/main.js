$(document).ready(function(){
    $('.modal').modal();
    $('.tooltipped').tooltip();
    $('[data-toggle="popover"]').popover();  
    $('.add-button').popover();  
    initializeColors()
    initializeHeights()
    $('.fixed-action-btn').floatingActionButton();

    // Project Focus Functionality
    $('.project-line').focusin(function(){
        var projectName = $(this).data('projectName');
        var action_buttons = $('.action-button');

        $(this).css('z-index',12);
        $('#fade').css('z-index',11);
        $('#fade').css('opacity',0.6);
        // take care of popovers, fade out
        $(this).popover('show');
        $(this).data('trigger','none');
        for (var i = action_buttons.length - 1; i >= 0; i--) {
            if ($(action_buttons[i]).data('projectName')===projectName) {
                
                // increase z-index
                $(action_buttons[i]).css('z-index',13);
                // open every popover
                $(action_buttons[i]).popover('show');
                // disable any accidental triggering 
                $(action_buttons[i]).unbind('mouseenter mouseleave');

            }
        }
        console.log($('.btn-floating').data('target'));
        $('div#create_project').css('z-index', 1);
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
        $('#title').attr('data-prev-title',"I'm working on " + "<font color=" + $(this).data('color') + ">" + $(this).data('projectName')+"</font>");
        $('#title').html("<font color=" + $(this).data('color') + ">" + $(this).data('projectName')+"</font>");
        $('#title').addClass('center')
        // date/login icon
        var prev = $('#icon').html()
        console.log(prev)
        $('#date').attr('data-prev-title',prev)
        $('#icon').remove()
        $('#date').html($(this).data('projectDate'));
        $('#date').addClass('light')

        // add delete link
        var del = "<a href='/remove_project/" + $(this).data('projectId') + "'>Delete Project?</a>"
        console.log(del)
        $("#delete").html(del)

        // unbind hover functionality
        $(this).unbind('mouseenter mouseleave');
    });
    $('.project-line').focusout(function(){
        var projectName = $(this).data('projectName');
        var action_buttons = $('.action-button');

        $('#fade').css('opacity',0);
        $('#fade').css('z-index',1);
        $(this).css('z-index',2);
        // take care of popovers
        $(this).popover('hide');
        for (var i = action_buttons.length - 1; i >= 0; i--) {
            if ($(action_buttons[i]).data('projectName')===projectName) {
                
                $(action_buttons[i]).removeClass('biggen');
                // decrease z-index
                $(action_buttons[i]).css('z-index',3)
                // close every popover
                $(action_buttons[i]).popover('hide')
                // enable regular triggering 
                $(action_buttons[i]).popover({ trigger: "manual" , html: true, animation:true})
                    .on("mouseenter", function () {
                        var _this = this;
                        $(this).popover("show");
                        $(".popover").on("mouseleave", function () {
                            console.log('wat')
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
                // rebind action-button hover functionality
                $(action_buttons[i]).hover(function(){

                    var color = $(this).data('color');
                    var y = color + "_shadow";
                    $(this).addClass(y);
                    $(this).addClass('biggen');
                    $('#title').attr('data-prev-title',$('#title').html());
                    $('#title').html("I'm working on " + "<font color=" + $(this).data('color') + ">" + $(this).data('projectName')+"</font>");
                }, function(){
                    var color = $(this).data('color');
                    var y = color + "_shadow";
                    $(this).removeClass('biggen');
                    $(this).removeClass(y);
                    $('#title').html($('#title').data('prevTitle'));
                });
            }   
        }
        console.log($('.btn-floating').data('target'));
        // $('div#create_project').css('z-index', 1000);
        $('.btn-floating').attr('data-tooltip',"Create Project");
        console.log($('.btn-floating').data('target'));
        var x = $(this).data('projectId');
        var color = $(this).data('color');
        var y = color + "_shadow";
        // action button colors
        $('.' + x).removeClass(y);
        $(this).removeClass(y);


        // fix title
        $('#title').html("I'm working on ...");
        $('#title').removeClass('center')
       // date/login icon
        prev = $('#date').attr('data-prev-title')
        $('#date').html(" ")
        $('#date').append("<li id='icon'>" + prev + "</li>")
        $('#date').removeClass('light')
        // remove delete link
        $("#delete").html(" ")

        // rebind project-line hover functionality
        $(this).hover(function(){
            var x = $(this).data('projectId');
            var color = $(this).data('color');
            var y = color + "_shadow";
            // action button colors
            $('.' + x).addClass(y);
            $(this).addClass(y);
            var projectName = $(this).data('projectName');
            var action_buttons = $('.action-button');
            for (var i = action_buttons.length - 1; i >= 0; i--) {
                if ($(action_buttons[i]).data('projectName')===projectName) {
                    $(action_buttons[i]).addClass('biggen');
                }
            }
            $(this).popover("show");
            $('#title').attr('data-prev-title',$('#title').html());
            $('#title').html("I'm working on " + "<font color=" + $(this).data('color') + ">" + $(this).data('projectName')+"</font>");
        }, function(){
            var x = $(this).data('projectId');
            var color = $(this).data('color');
            var y = color + "_shadow";
            // action button colors
            $('.' + x).removeClass(y);
            $(this).removeClass(y);
            $('#title').html($('#title').data('prevTitle'));
            $(this).popover("hide");
            var projectName = $(this).data('projectName');
            var action_buttons = $('.action-button');
            for (var i = action_buttons.length - 1; i >= 0; i--) {
                if ($(action_buttons[i]).data('projectName')===projectName) {
                    $(action_buttons[i]).addClass('biggen');
                }
            }
        });
    });
    $('#title').attr('data-prev-title',"I'm working on ...");
    // regular project-line hover functionality
    $('.project-line').hover(function(){
        var x = $(this).data('projectId');
        var color = $(this).data('color');
        var y = color + "_shadow";
        // action button colors
        $('.' + x).addClass(y);
        $(this).addClass(y);

        var projectName = $(this).data('projectName');
        var action_buttons = $('.action-button');
        for (var i = action_buttons.length - 1; i >= 0; i--) {
            if ($(action_buttons[i]).data('projectName')===projectName) {
                $(action_buttons[i]).addClass('biggen');
            }
        }
        var save = $('#title').html()
        $('#title').attr('data-prev-title',save);
        $('#title').html("I'm working on " + "<font color=" + $(this).data('color') + ">" + $(this).data('projectName')+"</font>");
    }, function(){
        var x = $(this).data('projectId');
        var color = $(this).data('color');
        var y = color + "_shadow";
        // action button colors
        $('.' + x).removeClass(y);
        $(this).removeClass(y);
        console.log($('#title').data('prevTitle'))
        $('#title').html($('#title').data('prevTitle'));
        var projectName = $(this).data('projectName');
        var action_buttons = $('.action-button');
        for (var i = action_buttons.length - 1; i >= 0; i--) {
            if ($(action_buttons[i]).data('projectName')===projectName) {
                $(action_buttons[i]).removeClass('biggen');
            }
        }
    });

    // reular action-button hover functionality
    $('.action-button').hover(function(){

        var color = $(this).data('color');
        var y = color + "_shadow";
        $(this).addClass(y);
        $('#title').attr('data-prev-title',$('#title').html());
        $(this).addClass('biggen');
        $('#title').html("I'm working on " + "<font color=" + $(this).data('color') + ">" + $(this).data('projectName')+"</font>");
        var theValue = $(this).data('actionId');
        console.log(theValue);
        $('.hidden_input_action_id').val(theValue);
        var url = './edit_action/' + theValue
        console.log(theValue)
        $('.editform').attr('action', url);
        console.log($('.editform').attr('action'))
    }, function(){
        var color = $(this).data('color');
        var y = color + "_shadow";
        $(this).removeClass(y);
        $(this).removeClass('biggen');
        $('#title').html($('#title').data('prevTitle'));
    });
  });


$('.add-button').on('click', function(){
    var theValue = $(this).data('projectName');
    console.log(theValue);
    $('.hidden_input').val(theValue);
});

// $('.add-button').on('click', function(){
//     var theValue = $(this).data('actionId');
//     console.log(theValue);
//     $('.hidden_input_action_id').val(theValue);
// });


function initializeColors(){
    var project_lines = $('.project-line');
    for (var i = project_lines.length - 1; i >= 0; i--) {
        var x = percentage($(project_lines[i]).data('projectName'));
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

function initializeHeights(){
    var project_lines = $('.project-line');
    var action_buttons = $('.action-button');
    for (var i = project_lines.length - 1; i >= 0; i--) {
        projectName = $(project_lines[i]).data('projectName');
        var count = 0;
        for (var j = action_buttons.length - 1; j >= 0; j--) {
            if ($(action_buttons[j]).data('projectName') === projectName) {
                count++;
            }
        }
        var height =  String(parseInt((count-1)*75)) + "px";
        $($(project_lines[i])).css("height", height);
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

$(".pop").popover({ trigger: "manual" , html: true, animation:true})
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