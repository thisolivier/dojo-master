function printSkip(start, end, skip = 1){
    if (end === undefined){
        end = start;
        start = 0;
    }
    for (var i = start; i < end; i += skip){
        console.log(i);
    }
    return;
}

printSkip(-10, 20, 5.5);