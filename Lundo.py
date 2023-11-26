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

    def addFoodToEquipment(self, food):
        self.equipment.addFood(food)

    def addMedToEquipment(self, medicine):
        self.equipment.addMedicine(medicine)

    def eat(self):
        print("Here is the list of your food:")
        self.equipment.getListOfFood()
        foodName = input("What do you wanna eat today????")
        food = self.equipment.getFood(foodName)
        if food:
            self.changeHunger(10)
            self.changeEnergy(10)
        else:
            print("You need to buy something!")

    def useMedicine(self):
        print("Here is the list of your medicine")
        self.equipment.getListOfMeds()
        medicineName = input("Owww you're ill? Try to use some medicine!")
        med = self.equipment.getMedicine(medicineName)
        if med:
            self.changeHealth(10)
            self.changeEnergy(-10)
        else:
            print("Try sth else!")

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

    def changeHealth(self, ammount):
        if self.health + ammount <= 100 and self.health + ammount >= 0:
            self.health += ammount
    
    def changeEnergy(self, ammount):
        if self.energy + ammount <= 100 and self.energy + ammount >= 0:
            self.energy += ammount

    def changeHunger(self, ammount):
        if self.hunger + ammount <= 100 and self.hunger + ammount >= 0:
            self.hunger += ammount

    def status(self):
        return f"{self.name}'s status:\nHunger: {self.hunger}\nHygiene: {self.hygiene}\nHealth: {self.health}\nFun: {self.fun}\nEnergy: {self.energy}\nMoney: {self.money}\n"