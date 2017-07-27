$(document).ready(function(){

    function makePokemon(many){
        var baseAPI = 'http://pokeapi.co/media/img/';
        for(var i = 1; i <= many; i++) {
            var pokemon = "<img class='pokemon' src=\"" + baseAPI + i + ".png\" alt=\"a pokemon\" pokeIndex=\""+ i +"\">";
            $('body').append(pokemon);
        }
    }

    function openPokedex(event){
        var pokeURL = 'http://pokeapi.co/api/v2/pokemon/' + $(this).attr('pokeIndex');
        var pokeIMG = $(this).attr('src');
        $('#pokedex').css('top','0');
        beginAnimation();
        $.getJSON(pokeURL, function(data){
            bootPokedex(data, pokeIMG);
        } );
    }

    function bootPokedex(pokeData, imgSRC){
        var htmlSections = [];
        var types = [];
        console.log (pokeData);
        for (val of pokeData.types){
            var typeItem = '<li>'+ val.type.name +'</li>';
            types.push(typeItem);
        }
        htmlSections[0] = '<div><img src="' + imgSRC + '" alt="Picture of pokemon' + pokeData.name + '">';
        htmlSections[0] += '<h2 class="pokeName">' + pokeData.name + '</h2></div>';
        htmlSections[1] = '<div><h3 class="types">Types</h3> <ul>' + types.join('') + '</ul>';
        htmlSections[1] += '<h3 class="height">Height</h3><p>' + pokeData.height + '</p>';
        htmlSections[1] += '<h3 class="weight">Weight</h3><p>' + pokeData.weight + '</p></div>';
        for (index in htmlSections){
            $('.screen').append(htmlSections[index]);
        }
        stopAnimation();
    }

    var animation;
    var switcher = true;

    function beginAnimation() {
        animation = setInterval(
            function(){ theAnimation() },
            500
        );
    }

    function stopAnimation() {
        clearInterval(animation);
        $('.buttons1 .dot:first-of-type').css('background-color','red');
        $('.buttons1 .dot:last-of-type').css('background-color','red');
    }

    function theAnimation(){  
        if (switcher) {
            $('.buttons1 .dot:first-of-type').css('background-color','white');
            $('.buttons1 .dot:last-of-type').css('background-color','red');
            switcher = false;
        } else {
            $('.buttons1 .dot:first-of-type').css('background-color','red');
            $('.buttons1 .dot:last-of-type').css('background-color','white');
            switcher = true;
        }
    }

    $('body').on('click', '.pokemon', function(){
        openPokedex.call(this, event);
        var this2 = $(this);
    })

    $('body').on('click', '.close', function(){
        $('#pokedex').removeAttr('style');
        $('.screen').html('');
    })

    makePokemon(151);
});