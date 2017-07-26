$(document).ready(function(){
    $('form').submit(function(event){
        event.preventDefault();
        var formData = $('form').serialize().split("&");
        var formObj = {};
        for (var idx = 0; idx < formData.length; idx++) {
            var itemData = formData[idx].split("=");
            formObj[itemData[0]] = itemData[1];
        }
        console.log(formObj);
        makeCard(formObj);
    })

    
});

function makeCard(person) {
    var newCard = $('.card').first().clone();
    $(newCard).children('h2').text(person.first_name + " " + person.last_name);
    $(newCard).children('.back').text(person.description);
    $('.cards').append(newCard);
}