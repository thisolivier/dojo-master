function whatTimeIsIt (HOUR, MINUTE, PERIOD) {
    var timeOfDay = PERIOD == "AM" ? " in the morning" : " in the evening";
    if (PERIOD == "PM") {
        if (HOUR < 6) timeOfDay = " in the afternoon";
        if (HOUR > 9) timeOfDay = " at night";
    }

    if (HOUR == 12 && MINUTE == 0){
        var noonMidnight = PERIOD == "AM" ? "noon" : "midnight";
        console.log("It's 12:00 " + noonMidnight);
        return;
    }

    if (MINUTE == 15 || MINUTE == 45) {
        var toOrPast = MINUTE == 15 ? "past " : "to ";
        if (MINUTE == 45) HOUR += 1;
        console.log("It's quater "+ toOrPast + (HOUR) + timeOfDay );
    } else if (MINUTE == 5 || MINUTE == 55) {
        var toOrPast = MINUTE == 5 ? "to " : "past ";
        if (MINUTE == 55) HOUR -= 1;
        console.log("It's 5 "+ toOrPast + (HOUR) + timeOfDay );
    } else if (MINUTE > 30){
        console.log("It's almost "+ (HOUR + 1) + timeOfDay );
    } else {
        console.log("It's just after "+ HOUR + timeOfDay );
    }
}

whatTimeIsIt(8,50,"AM");