function makeFancy(arr, arrow = " -> ", reserved = false) {
    if (!reserved) {
        for (var i = 0; i < arr.length; i++){
            console.log(i + arrow + arr[i]);
        }
    } else {
        for (var i = arr.length -1; i <= 0; i--){
            console.log(i + arrow + arr[i]);
        }
    }
}

makeFancy(["john","jilly","gilgamesh"], " <--> ", true);