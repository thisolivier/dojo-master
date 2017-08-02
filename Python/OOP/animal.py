class Animal(object):
    def __init__ (self, name="Generic Animal", health=50):
        self.name = name
        self.health = int(health)
    
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

    def pet(self):
        self.health += 5
        return self

class Dragon(Animal):
    def __init__ (self, name = "Generic Dragon", health = 170):
        super(Dragon, self).__init__(name, health)

    def fly(self):
        self.health -= 10
        return self
    
    def displayHealth(self):
        super(Dragon, self).displayHealth()
        print "I am a Dragon"

myAnimal = Animal("Snakey", 200)
myDog = Dog("Barry")
myDragon = Dragon("Beetle")

myDog.walk().walk().walk().run().run().pet().displayHealth()
myDragon.fly().run().run().fly().displayHealth()