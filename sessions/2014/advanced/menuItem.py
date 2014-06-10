class MenuItem:
    'Common base for all food items'
    def __init__(self, name, price):
            self.name = name
            self.price = price
    def displayMenuItem(self):
            print ("Name: ", self.name, ", Price: ", self.price)

if __name__ == "__main__":
	item1 = MenuItem("Rice",5)
	item1.displayMenuItem()
