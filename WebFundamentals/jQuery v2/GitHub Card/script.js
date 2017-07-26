$(document).ready(function(){
    $('form').submit(function(event){
        event.preventDefault();
        getData();
    })

    $('.cards').on('click', '.card', function(){
        swapContent.apply(this);
    })
});

function getData(){
    var username = $('input[name="username"]').val();
    console.log(username);
    var url = 'https://api.github.com/users/' +  username;
    $.getJSON(url, function(data){
         makeCard(data);
    })
}

function makeCard(userObj) {
    console.log(userObj);
    var newCard = $('.card').first().clone();
    var newName = userObj.name;
    newCard.find('h2').text(newName);
    newCard.children('.back').text(userObj.bio);
    newCard.children('.back').prepend('<img src="' + userObj.avatar_url + '"><br>');
    $('.cards').append(newCard);
}

function swapContent(){
    $(this).children('.front').slideToggle();
    $(this).children('.back').slideToggle();
}

// $('form').submit(function(event){
//     event.preventDefault();
//     var username = $('input[name="username"]').val();
//     var url = 'https://api.github.com/users/' +  username
//     $.getJSON(url, function(data){
//         random(data);
//     });
//     console.log(username);
// });

// function random(event){
//     alert("boo");
// }