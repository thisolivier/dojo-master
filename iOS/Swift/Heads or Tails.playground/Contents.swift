//: Playground - noun: a place where people can play

import UIKit

var str = "Hello, playground"

func tossCoin() -> String {
    print ("Tossing a coin")
    var result = "Heads"
    let random = Int(arc4random_uniform(2))
    if random == 1 {
        result = "Tails"
    }
    print (result)
    return result
}

tossCoin()

func tossMultipleCoins(xTimes:Int) -> Double {
    var headCount:Double = 0
    for _ in 0...xTimes{
        if tossCoin() == "Heads" {
            headCount += 1
        }
    }
    let xTimes = Double(xTimes)
    return headCount / xTimes
}

print (tossMultipleCoins(xTimes: 20))