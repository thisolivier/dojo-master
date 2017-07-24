function fewBillion(days) {
    var total = 0,
        currentAdd = 0.01,
        hitJackpot = [false, false];

    for (var i = 0; i < days; i++){
        if(total >= 10000 && !hitJackpot[0] ) {
            console.log("Reached $10,000 at " + i + " days.");
            hitJackpot[0] = true;
        } else if (total >= 1000000000 && !hitJackpot[1] ) {
            console.log("Reached $ ONE BILLION $ at " + i + " days.");
            hitJackpot[1] = true;
        } else if (total == Infinity ) {
            console.log("Reached infinity at " + i + " days.");
            return;
        }
        total += currentAdd;
        currentAdd *= 2;
    }
    return (total);
}

console.log(fewBillion(30));