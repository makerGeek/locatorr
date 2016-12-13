
//import jQuery
var script = document.createElement('script');
script.src = 'https://code.jquery.com/jquery-1.11.0.min.js';
script.type = 'text/javascript';
document.getElementsByTagName('head')[0].appendChild(script);


//post login
$.ajax({
    type: 'POST',
    // make sure you respect the same origin policy with this url:
    // http://en.wikipedia.org/wiki/Same_origin_policy
    url: 'http://127.0.0.1:8000/accounts/login/',
    data: { 
        'username': 'aaa', 
        'password': '123123aze'
    },
    success: function(msg){
        alert('wow' + msg);
    }
});


//get groups
$.get( "http://127.0.0.1:8000/index/api/welcome", function( data ) {
  console.log(data);
  alert( "Load was performed." );
});