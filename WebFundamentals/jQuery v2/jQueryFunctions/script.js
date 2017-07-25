$(document).ready(function(){
    $('#begin').click(function(){
        $('.wrapper').show();
    })

    $('.square').click(function(){
        $(this).addClass('round');
    })

    $('.yellow').click(function(){
        $(this).slideToggle();
    })

    $('.green').click(function(){
        $(this).fadeOut();
    })

    $('#reveal').click(function(){
        $('.card').show();
    })

    $('#append').on('click', 'h2', function(){
        var classList = $(this).closest('.card').attr('class');
        $(this).closest('.card').append('<p>' + classList + '</p>');
    })
});