$(document).ready(function(){
    function makePokemon(many){
        var baseAPI = 'http://pokeapi.co/media/img/';
        for(var i = 1; i <= many; i++) {
            var pokemon = "<img src=\"" + baseAPI + i + ".png\" alt=\"a pokemon\">";
            $('body').append(pokemon);
        }
    }

    makePokemon(151);
});