class Bike(object):
    def __init__(self, pri, spd, mle = 0):
        self.price = pri
        self.max_speed = spd
        self.miles = mle

    price = None
    max_speed = None
    miles = None

    def displayInfo (self) :
        string = "\nBike Stats\n-------\nPrice: {}\nTop Speed: {}\nMileage: {}\n"
        print string.format(self.price, self.max_speed, self.miles)
        return self

    def ride (self) :
        print "Riding in progress..."
        self.miles += 10
        return self

    def reverse (self) :
        if self.miles >= 5 :
            print "BACKING UP!"
            self.miles -= 5
        else:
            print "You have reached the beginning of side one."
        return self

hot_rod = Bike("200", "35mph")
slayer = Bike("20", "20mph")
mama_cow = Bike("300", "20mph")

hot_rod.ride().ride().ride().reverse().displayInfo()

slayer.ride().ride().reverse().reverse().displayInfo()

mama_cow.reverse().reverse().reverse().displayInfo()