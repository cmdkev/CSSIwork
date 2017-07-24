function howMuchMoney() {
  var input_text = $('input').val();
  $('#result').text(200 * input_text + " gold dragons");
  alert(200 * input_text + " gold dragons")
}

$(document).ready(function() {
  $('#dragons').click(howMuchMoney)
})
