$(document).ready(function(){
    $(document).keydown(function(event){
        event.preventDefault;
        callMove(whatDirection(event));
    })
});

function whatDirection(event){
    var vector = 0;
    switch (event.which) {
        case 37:
            vector = 4;
            break;
        case 38:
            vector = 1;
            break;
        case 39:
            vector = 2;
            break;
        case 40:
            vector = 3;
            break;
        default: 
            break;
    }
    return vector;
}

function callMove(direction){
    var xPos = $('.pacpac').nextAll().length;
    var yPos = $('.pacpac').parent().nextAll().length;
    console.log("X = " + xPos + ". Y = " + yPos);
    console.dir($('.pacpac').nextAll());
}

// When get move,
//     When pacperson is in middle of square,
//         Change direction to new move
    
// When have direction
//     Pacperson position moves at constant velocity in direction
//     When pacperson current square is coin
//         Coin replaced with empty
//         Score increased
//     When next square is wall
//         pacperson should stop
//     When current square is ghost
//         pacperson dies