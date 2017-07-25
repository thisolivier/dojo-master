$(document).ready(function(){
    $('img').click(function(){
        $(this).hide();
    });

    $('#lazarus').click(function(){
        $('img').show();
    });
});