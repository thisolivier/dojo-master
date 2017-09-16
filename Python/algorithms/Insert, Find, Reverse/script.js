/********************/
/* Reverse an array */
/********************/

function reverse(arr){
    var length = arr.length -1;
    for (var i = 0; i < length /2; i++ ){
        var temp = arr[i]
        arr[i] = arr[length - i]
        arr[length - i] = temp
    }
    return arr
}

my_array = [1,2,3,23,1,4]
console.log (reverse(my_array));

/********************/
/* Find in an array */
/********************/

function find(arr, int){
    var length = arr.length;
    var index = -1;
    for (var i = 0; i < length; i++ ){
        if (arr[i] == int){
            index = i
        }
    }
    return index
}

my_array2 = [1,23,3,4]
console.log (find(my_array2, 23));

/************************/
/* Insert into an array */
/************************/

function insert(arr, ind, num){
    length = arr.length -1;
    for (var i = length; i >= ind; i--){
        // This line is key
        // You're extending the array and shifting the array to fill that. 
        arr[i+1] = arr[i]
    }
    arr[ind] = num
    return arr
}

my_array3 = [1,23,3,4]
console.log (insert(my_array3, 1, 62));