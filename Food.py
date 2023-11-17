class Food:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def feed(self):
        if self.quantity > 0:
            self.quantity -= 1
            return 10
        else:
            print("No food left!")
            return 0