$(document).ready( function() {

    $('.tank-action').on('mousedown touchstart', function(e) {
        $.ajax({ 
            url: '/tank/move/', 
            data: { 'action' : $(this).data("action"), 'duration': 1 }, 
        });
      });//.bind('mouseup mouseleave touchend', function() {});

});