$(document).ready(function(){
    $('.houses img').click(function(){
        $('.housedetails').css('opacity',100)
        var theHouse = houses[$(this).attr('house')];
        $('#name').text(theHouse.name);
        $('#words').text(theHouse.words);
        $('#titles').text(theHouse.titles.join(", "));
    })

    var houses = {
        '17' : {}, 
        '229' : {}, 
        '362' : {}, 
        '378' : {}
    };

    $.each(houses, function(key){
        var url = 'https://anapioficeandfire.com/api/houses/' + (key);
        $.getJSON(url,  function(data){
            houses[key] = data;
        })
    })
});