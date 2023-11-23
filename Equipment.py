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
        print(self.foodList)