//: Playground - noun: a place where people can play

import UIKit

class Animal{
    var Name:String
    var Health = 100
    
    init(newName:String, maybeHealth:Int?){
        if let newHealth = maybeHealth{
            self.Health = newHealth
        }
        self.Name = newName
    }
    
    func displayHealth() -> Int{
        print("The \(NSStringFromClass(type(of: self))) called \(self.Name) has a health of \(self.Health)")
        return self.Health
    }
}

class Cat:Animal{
    init(catName:String){
        super.init(newName: catName, maybeHealth: 150)
    }
    
    func Growl(){
        print ("Toot")
    }
    
    func Run(){
        print ("Cat go fast")
        self.Health -= 10
    }
}

class Lion:Cat{
    override func Growl(){
        print ("The lion says... BOOM! Shake shake shake the room.")
    }
    
    init(lionName:String){
        super.init(catName: lionName)
        self.Health = 200
    }
    
}

class Cheetah:Cat{
    override func Run() {
        if self.Health >= 50 {
            print ("Cat go very very fast")
            self.Health -= 50
        } else {
            print ("Too fat, need sleep")
        }
    }
    
    func Sleep(){
        print ("I might not be a lion, but it sounds like music when I sleep.")
        self.Health += 50
        if self.Health > 200{
            self.Health = 200
        }
    }
}

var bestCheat = Cheetah(catName: "King Cheesy")
bestCheat.Run()
bestCheat.Run()
bestCheat.Run()
bestCheat.Run()
bestCheat.displayHealth()

print(" ")

var okLion = Lion(lionName: "Prince Joey")
okLion.Run()
okLion.Run()
okLion.Run()
okLion.Growl()
