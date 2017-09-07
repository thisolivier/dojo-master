//: Playground - noun: a place where people can play

import UIKit

enum Cols: Int {
    case Red = 1, Green, Blue
}

struct Card{
    let Color: Cols
    let Roll: Int
    
    init(cardCol: Cols) {
        self.Color =  cardCol
        let roll = Int(arc4random_uniform(2))
        
        var options:[Int]!
        
        switch Color{
        case .Red:
            options = [1,2]
        case .Green:
            options = [3,4]
        case .Blue:
            options = [5,6]
        }
        self.Roll = options[roll]
    }
    
    var description: String {
        return ("[\(Color), \(Roll)]")
    }
}

class Deck{
    var Cards: [Card] = []
    
    init(){
        for index in 1...3{
            let currentColor = Cols(rawValue: index )!
            for _ in 1...10{
                self.Cards.append(Card(cardCol: currentColor))
            }
        }
        print ("We have \(self.Cards.count) of cards in our Deck")
    }
    
    func Deal() -> Card?{
        if !self.IsEmpty(){
            return self.Cards.remove(at: self.Cards.count - 1)
        }
        return nil
    }
    
    func IsEmpty() -> Bool{
        if self.Cards.count == 0 {
            return true
        }
        return false
    }
    
    func Shuffle(){
        let zeroIndexCards = self.Cards.count-1
        func newPosFromTotal(total:Int, used:Int) -> Int{
            let range = UInt32(total - used)
            let rangeRand = Int(arc4random_uniform(range))
            return rangeRand + used
        }
        
        for index in 0 ... zeroIndexCards{
            let newPos = newPosFromTotal(total: zeroIndexCards, used: index)
            let tempCard = self.Cards[newPos]
            self.Cards[newPos] = self.Cards[index]
            self.Cards[index] = tempCard
        }
    }
    
    func PrintDeck(){
        print("Deck as follows ---")
        var toPrint = ""
        for card in self.Cards{
            toPrint += "[\(card.Color) \(card.Roll)]"
        }
        print (toPrint)
    }
}

class Playa{
    var name:String
    var hand:[Card] = []
    
    init(newName:String){
        self.name = newName
        print ("Player \(newName) has joined the game")
    }
    
    func DrawFromDeck(myDeck:Deck) -> Card?{
        if let newCard = myDeck.Deal(){
            self.hand.append(newCard)
            return newCard
        }
        return nil
    }
    
    func RollDice() -> Int{
        let diceRoll = Int(arc4random_uniform(5)) + 1
        return diceRoll
    }
    
    func MatchingCards(corColor:Cols, corRoll:Int) -> Int{
        var count = 0
        for card in hand {
            if card.Color == corColor && card.Roll == corRoll {
                count += 1
            }
        }
        return count
    }
}

func testPlaya(){
    let theDeck = Deck()
    theDeck.Shuffle()
    theDeck.PrintDeck()
    print(" ")
    let thePlaya = Playa(newName: "Joe Bloggs")
    print ("\(thePlaya.name) drew a \(thePlaya.DrawFromDeck(myDeck: theDeck)!.description)")
    print ("\(thePlaya.name) drew a \(thePlaya.DrawFromDeck(myDeck: theDeck)!.description)")
    print ("\(thePlaya.name) drew a \(thePlaya.DrawFromDeck(myDeck: theDeck)!.description)")
    print ("\(thePlaya.name) drew a \(thePlaya.DrawFromDeck(myDeck: theDeck)!.description)")
    print ("\(thePlaya.name) drew a \(thePlaya.DrawFromDeck(myDeck: theDeck)!.description)")
    print ("\(thePlaya.name) drew a \(thePlaya.DrawFromDeck(myDeck: theDeck)!.description)")
    print ("\(thePlaya.name) rolled a \(thePlaya.RollDice())")
    
    if let scaryCard = theDeck.Deal() {
        let matches = thePlaya.MatchingCards(corColor: scaryCard.Color, corRoll: scaryCard.Roll)
        print ("Joe has \(matches) cards matching \(scaryCard.description)")
    } else {
        print("No cards left")
    }
}

testPlaya()
