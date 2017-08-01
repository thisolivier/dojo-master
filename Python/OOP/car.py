class Car(object):
    def __init__ (self, price, speed, milage, fuel):
        self.price = price
        self.tax = "15%" if price > 10000 else "12%"
        self.speed = speed
        self.milage = milage
        self.fuel = fuel
        self.display_all()
    
    def display_all(self):
        print "\nCar Upcoming\n-------\n"
        print "Price: ", self.price
        print "Speed: {}mph".format(self.speed)
        print "Fuel:", self.fuel
        print "Mileage: {}mpg".format(self.milage)
        print "Tax: ",self.tax
        print "\n"
        return self

mini = Car(500, 60, 20000, "full")
jaguar = Car(20000, 100, 9000, "empty")
chevy = Car(50, 20, 200000, "A little bit")
mini2 = Car(600, 30, 30000, "Two thirds full")
jaguar2 = Car(60000, 90, 7000, "10 miles")
chevy2 = Car(60, 40, 10000, "Beans")
