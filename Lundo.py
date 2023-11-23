from Equipment import Equipment
class Lundo:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.hygiene = 50
        self.health = 100
        self.fun = 50
        self.energy = 50
        self.money = 0
        self.equipment = Equipment()

    def addToEquipment(self, food):
        self.equipment.addFood(food)

    def eat(self):
        foodName = input("What do you wanna eat today????")
        food = self.equipment.getFood(foodName)
        if food:
            self.hunger += 10
            self.energy += 5
        else:
            print("You need to buy something!")

    def play(self):
        self.fun += 10
        self.energy -= 10

    def sleep(self):
        self.energy += 20

    def work(self):
        self.money += 10
        self.energy -= 10
        self.fun -= 5

    def bath(self):
        self.hygiene += 10
        self.energy -= 5

    def increase_health(self, amount):
        self.health += amount

    def decrease_hygiene(self, amount):
        self.hygiene -= amount

    def increase_hygiene(self, amount):
        self.hygiene += amount


    def increase_energy(self, amount):
        self.energy += amount

    def decrease_hunger(self, amount):
        self.hunger -= amount

    def decrease_money(self, amount):
        self.money -= amount
        

    def status(self):
        return f"{self.name}'s status:\nHunger: {self.hunger}\nHygiene: {self.hygiene}\nHealth: {self.health}\nFun: {self.fun}\nEnergy: {self.energy}\nMoney: {self.money}\n"