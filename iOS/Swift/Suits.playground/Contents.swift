let suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
let cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
var deckOfCards = [String: [Int]]()

func buildDeckFromEmpty(deck: inout[String: [Int]]){
    for suit in suits {
        let set:[Int] = cards
        deck[suit] = set
    }
}

buildDeckFromEmpty(deck: &deckOfCards)

print(deckOfCards)
