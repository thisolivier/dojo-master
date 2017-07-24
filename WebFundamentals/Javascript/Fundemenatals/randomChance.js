function slots(plays, stopper = false){
    var rewardValue = Math.ceil(Math.random()*50) + 50;
    while (plays > 0){
        plays--;
        if (Math.ceil(Math.random()*100) === 100) {
            plays = plays + rewardValue;
            console.log("Winner winner, chicken dinner! You haven " + (plays) + " quaters");
            if (!stopper || (stopper && plays >= stopper)) return plays;
            rewardValue = Math.ceil(Math.random()*50) + 50;
        }
    }
    return 0;
}
console.log(slots(200,300));