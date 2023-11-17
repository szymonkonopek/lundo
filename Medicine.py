class Medicine:
    def __init__(self, name, quantity, healthCount):
        self.name = name
        self.quantity = quantity
        self.healthCount = healthCount

    def use(self):
        if self.quantity > 0:
            self.quantity -= 1
            return self.healthCount
        else:
            return 0