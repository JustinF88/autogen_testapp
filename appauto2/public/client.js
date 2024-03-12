// client-side js
// run by the browser each time your view template is loaded

// by default, you've got jQuery,
// add other scripts at the bottom of index.html

$(function() {
  console.log('hello world :o');
  
  //$.get('/dreams', function(dreams) {
  //  dreams.forEach(function(dream) {
  //    $('<li></li>').text(dream).appendTo('ul#dreams');
  //  });
  //});

/* No longer using this, combined to post/ get functionality to 1 function
  function get_func(){
  $.get('/dreams_get').done(function(dreams) {
    console.log("these are the dreams" );
    console.log(dreams);
    $('<li><b></b></li>').text(dreams[0]).appendTo('ul#dreams');
    dreams.shift();
    dreams.forEach(function(dream) {
    $('<li></li>').text(dream).appendTo('ul#dreams');

    });
  });   
  }; // end of get_func

*/

  $('form').submit(function(event) {
    event.preventDefault();
    dream = $('input').val();
    d = $('<li></li>');
    d.addClass('libold');
    d.text(dream);
    d.appendTo('ul#dreams');
    console.log("this is the dream");
    console.log(dream);
    $.post('/dreams?' + $.param({'dream': dream})).done(function(dreams) {
      console.log("these are the dreams" );
      console.log(dreams);
      dreams.shift();
      dreams.forEach(function(dream) {
        d = $('<li></li>');
        d.addClass('lireg');
        d.text(dream);
        d.appendTo('ul#dreams');
  
  
        
      });
    })
})

$(document).on('click','#workflow',function(){
  var num_ag = $("#num_agents").val();
  console.log(num_ag);
  $.post('/workflow?' + $.param(
    {'newworkflow': "hello test",
    'num_ag': num_ag

}));
  

});

});