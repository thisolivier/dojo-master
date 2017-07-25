$(document).ready(function(){
    $('img').click(function(){
        var imgSrc = $(this).attr('src');
        $(this).attr('src', $(this).attr('standby'));
        $(this).attr('standby', imgSrc);
    })
});