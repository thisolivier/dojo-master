$(document).ready(function(){

    $('form').submit(function(event){
        event.preventDefault();
        var result = $('form').serialize().split("&");
        $('tbody').append("<tr>");
        for (var i = 0; i < result.length; i++) {
            var item = result[i].split("=");
            $('tbody').append("<td>" + item[1] + "</td>");
        }
        $('tbody').append("</tr>");
    });
});