function numbersExclusive(arr){
    var newArray = []
    for (var i=0; i < arr.length; i++){
        if (typeof arr[i] === "number") newArray.push(arr[i]);
    }
    return newArray;
}

function numbersKiller(arr){
    var newArray = []
    for (var i=0; i < arr.length; i++){
        if (typeof arr[i] !== "number") newArray.push(arr[i]);
    }
    for (var i = 0; i < newArray.length; i++){
        arr[i] = newArray[i]
    }
    arr.length = newArray.length;
    return arr;
}

function numbersKiller2(arr){
    for (var i = 0; i < arr.length; i++){
        if (typeof arr[i] === "number") {
            for (var j = i; j < arr.length; j++){
                arr[j] = arr[j+1];
            }
            arr.length = arr.length - 1;
        }
    }
    return arr;
}

var testArr = [0, "hello", true, 123]
console.log(numbersKiller(testArr));