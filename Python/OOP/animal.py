class Animal(object):
    def __init__ (self, name="Generic Animal", health=50):
        self.name = name
        self.health = int(health)

    def __repr__ (self):
        return "<User Animal object, name: '{}', methods .displayHealth() .walk() .run()>".format(self.name)
    
    def walk (self):
        self.health -= 1
        return self

    def run (self):
        self.health -= 5
        return self
    
    def displayHealth (self):
        print "\n{}'s health is: {}".format(self.name, self.health)
        return self

class Dog(Animal):
    def __init__ (self, name = "Generic Dog", health=150):
        super(Dog, self).__init__(name, health)

    def __repr__ (self):
        return "<User Dog object, name: '{}', methods .pet(), extends Animal .displayHealth() .walk() .run()>".format(self.name)

    def pet(self):
        self.health += 5
        return self

class Dragon(Animal):
    def __init__ (self, name = "Generic Dragon", health = 170):
        super(Dragon, self).__init__(name, health)

    def __repr__ (self):
        return "<User Dragon object, name: '{}', methods .fly(), extends Animal .displayHealth() .walk() .run()>".format(self.name)


    def fly(self):
        self.health -= 10
        return self
    
    def displayHealth(self):
        super(Dragon, self).displayHealth()
        print "I am a Dragon"

if __name__ == "__main__":

    myAnimal = Animal("Snakey", 200)
    myDog = Dog("Barry")
    myDragon = Dragon("Beetle")

    myDog.walk().walk().walk().run().run().pet().displayHealth()
    myDragon.fly().run().run().fly().displayHealth()
    print myAnimal
    print myDragon