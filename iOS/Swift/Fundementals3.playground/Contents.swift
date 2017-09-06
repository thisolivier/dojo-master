//: An app to build and shuffle an array of numbers, then work out where the meaning of life is.

import UIKit

var numBank: [Int] = []

func buildDeckFromEmpty(deck: inout [Int]){
    
    func Shuffle(deck: inout [Int]){
        let dummy1 = Int(arc4random_uniform(255))
        let dummy2 = Int(arc4random_uniform(255))
        let temp = deck[dummy1]
        deck[dummy1] = deck[dummy2]
        deck[dummy2] = temp
    }
    
    for idx in 1...255 {
        deck.append(idx)
        if idx == 255 {
            for _ in 1...100 {
                Shuffle(deck: &deck)
            }
        }
    }
}

func removeMeaningFrom(deck: inout [Int]){
    for idx in 1...deck.count {
        if deck[idx] == 42 {
            print ("We found the answer to the Unltimate Question at position \(idx)")
            deck.remove(at: idx)
            break;
        }
    }
}



buildDeckFromEmpty(deck: &numBank)
removeMeaningFrom(deck: &numBank)

