function birthdayCount(daysRemaining) {
    if (daysRemaining < 0) return ("Negative days not allowed, better luck next year");
    while(daysRemaining > 30) {
        console.log("Sad times, it's ages until your birthday, " + daysRemaining + " days. :(");
        daysRemaining-=1;
    }
    while(daysRemaining > 0) {
        console.log("Only " + daysRemaining + " days to go!");
        daysRemaining-=1;
    }
    console.log("WOOOOOOOOOOO!");
    console.log("Birthday Time!");
}