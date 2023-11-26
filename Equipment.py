from Food import Food

class Equipment:
    def __init__(self):
        self.foodList = []
        self.medicineList = []

    def addFood(self, food): 
        self.foodList.append(food)

    def getFood(self, name):
        for index, food in enumerate(self.foodList):
            if (food.getName() == name):
                self.foodList.pop(index)
                return food
    
    def getListOfFood(self):
        for food in self.foodList:
            print(food.getName())

    def getListOfMeds(self):
        for med in self.medicineList:
            print(med.getName())

    def addMedicine(self, medicine): 
        self.medicineList.append(medicine)

    def getMedicine(self, name):
        print("hllo")
        for index, med in enumerate(self.medicineList):
            if (med.getName() == name):
                self.medicineList.pop(index)
                return med
    
