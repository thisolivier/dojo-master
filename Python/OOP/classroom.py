class Classroom(object):
    def __init__(self, name = "Generic Classroom"):
        self.name = name
        self.room = []
    
    def add(self, childObj):
        if isinstance(childObj, Kid):
            self.room.append(childObj)
        else:
            print "Not a child"
        return self

    def allSpeak(self):
        print "\nRoll Call!\n-------"
        for child in self.room:
            child.speak();
        return self

class Kid(object):
    def __init__ (self, first = "GenericFirst", last = "GenericLast"):
        self.first = str(first).title()
        self.last = str(last).title()

    def speak(self):
        print "My name is {}".format(self.first, self.last)

kid1 = Kid("Who")
kid2 = Kid("What")
kid3 = Kid(" ")
kid4 = Kid("Chika-chika Slim Shady")

smallRoom = Classroom("2A")
smallRoom.add(kid1).add(kid2).add(kid3).add(kid4).allSpeak()