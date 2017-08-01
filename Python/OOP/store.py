import product

class Store (object):
    def __init__(self, products = [], location = "123 Address Park", owner = "Joe Blogs"):
        self.products = products
        self.location = location
        self.owner = owner

    def add_product (self, price, itemName, weight, brand, cost, status):
        newProduct = product.Product(price, itemName, weight, brand, cost, status)
        self.products.append(newProduct)

    def remove_product (self, productName):
        for index, product in enumerate(self.products):
            if product.itemName == productName:
                self.products.pop(index)
    
    def inventory (self):
        for product in self.products:
            product.displayInfo()



myStore = Store()
myStore.add_product(30, "Bannana", "1kg", "Organics", 0.5, "for sale")
myStore.add_product(20, "Stawberry", "0.1kg", "Sam's Farm", 0.1, "past best")
myStore.inventory()