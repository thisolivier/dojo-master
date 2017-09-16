//: Playground - noun: a place where people can play

for index in 1...255 {
    print (index)
}

for index2 in 1...100 {
    let divisible3 = (index2 % 3 == 0)
    let divisible5 = (index2 % 5 == 0)
    if (divisible3 || divisible5) && !(divisible5 && divisible3){
        print (index2)
    }
}

for index3 in 1...100 {
    let divisible3 = (index3 % 3 == 0)
    let divisible5 = (index3 % 5 == 0)
    if (divisible3 && divisible5){
        print ("C-c-c-COMBO")
    } else if divisible3 {
        print ("Buzz")
    } else if divisible5 {
        print ("Fizz")
    }
}