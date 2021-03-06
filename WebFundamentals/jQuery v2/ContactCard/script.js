$(document).ready(function(){
    $('form').submit(function(event){
        event.preventDefault();
        makeCard(seralizeData(event));
    })

    $('.cards').on('click', '.card', function(){
        swapContent.apply(this);
    })
});

function makeCard(person) {
    console.log(person);
    var newCard = $('.card').first().clone();
    var newName = person.first_name + " " + person.last_name;
    newCard.find('h2').text(newName);
    newCard.children('.back').text(person.description);
    $('.cards').append(newCard);
}

function seralizeData(event){
    var formData = $('form').serialize().split("&");
        var formObj = {};
        for (var idx = 0; idx < formData.length; idx++) {
            var itemData = formData[idx].split("=");
            formObj[itemData[0]] = itemData[1];
        }
        return formObj;
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