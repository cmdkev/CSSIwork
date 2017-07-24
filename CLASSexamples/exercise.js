//call its id/class in order to hide something --> $(__)
//.js functions have input and output like algebra


function disappear_reveal() {
//  $("#static").fadeOut("#static")
  $("#transition").fadeIn("#transition");
}

function typeStuff() {
  var input_text = $('input').val();
  $('#result').text(input_text);
  alert(input_text);
}
/*
function reset(){
  $("#static").fadeIn("#static")
  $("#transition").fadeOut("#transition");
}
*/
$(document).ready(function() {
    $("#static").hover(disappear_reveal);
    $('#BIGBUTT').click(typeStuff);
    }
)
/*
$(document).ready(function() {
    $('#BIGBUTT').click(typeStuff);
    }
)
*/
