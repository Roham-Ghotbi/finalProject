$(".action-button").on('click', function() {
        // move from list_todo container to list_doing container
        console.log("Im in here");

        // $(this).html("Add To To-Do");
        if ($(this).hasClass("done")) {
        	$(this).removeClass("done");
	        $(this).addClass("not_done");
        } else{
        	$(this).removeClass("not_done");
	        $(this).addClass("done");
        }
});

$( init );

function init() {
  $('#makeMeDraggable').draggable({cancel:false});
}