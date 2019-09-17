var myInterval = setInterval( calc_distance, 2000 );
var action  = "";

$(document).ready( function() {

    $('.tank-action').on('mousedown touchstart', function(e) {
        action = $(this).data("action");
        
        $.ajax({ 
            url: '/tank/move/', 
            data: { 'action' : action, 'duration': 1 }, 
        });
      });//.bind('mouseup mouseleave touchend', function() {});

});


function calc_distance( ){
    
    if ( action.length < 1 ) return;
    
    if ( $.inArray(action, ['b','br','bl']) !=-1 ){ //calc distance when moving backwords
        $.ajax({ 
            url: '/tank/distance/', 
            success: function( response ){
                $("#camera-info").text(response + "m");
            }
        })
    } else {
        $("#camera-info").text("");
    }
}