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

  function get_func(){
  $.get('/dreams_get').done(function(dreams) {
    console.log("these are the dreams" );
    console.log(dreams);
    dreams.forEach(function(dream) {
    $('<li></li>').text(dream).appendTo('ul#dreams');


      
    });
  });   
  }; // end of get_func



  $('form').submit(function(event) {
    event.preventDefault();
    dream = $('input').val();
    console.log("this is the dream");
    console.log(dream);
    $.post('/dreams?' + $.param({'dream': dream})).done(get_func())
  
  



})});