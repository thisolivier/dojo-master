class Product(object):
    def __init__(self, price, itemName, weight, brand, cost, status = "for sale"):
        self.price = price
        self.itemName = itemName
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = status
    
    def sell(self):
        if (self.status != "sold") :
            self.status = "sold"
        else :
            print "Err - Product is already marked as sold."
        return self
    
    def addTax(self, tax):
        return float(self.cost) + (float(self.cost) * float(tax))

    def returns(self, string):
        if string.find('defective') >= 0 :
            self.status = "defective"
            self.price = 0
        elif string.find('in the box') >= 0 :
            self.status = "used"
            self.price = float(self.price) * 0.8
        return self
    
    def displayInfo(self):
        print "\n{} Details Upcoming\n-------\n".format(self.itemName)
        print "Price:",self.price
        print "Name:",self.itemName 
        print "Weight:",self.weight
        print "Brand:",self.brand
        print "Cost:",self.cost
        print "Status:",self.status
        return self
    
lamp = Product(20, 'Best Lamp', '20kg', 'IHOP', '30')

print lamp.displayInfo().addTax(0.1)

lamp.displayInfo().returns("Returned in the box").displayInfo()