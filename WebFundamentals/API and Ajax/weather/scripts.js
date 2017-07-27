$(document).ready(function(){
    $('form').submit(function(e){
        e.preventDefault();
        var city = $('#cityField').val();
        var key = '&APPID=9111c6482d7e20465b6ff5477a809fa3';
        var url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city + key;
        $.get(url, function(data){ addCity(data) });
    });
});

function addCity(data){
    console.dir(data);
    var newString = '<div class="cityResult"><h2>' + data.name +'</h2>'
    newString += '<span>Temperature: ' + (Math.floor((data.main.temp - 273.15) * 10)/10) +'&#8451;</span>'
    newString += '</div>'
    $('body').append(newString);
}
