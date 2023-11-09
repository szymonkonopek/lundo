import random

class GuessNumber:
    def __init__(self):
        self.number = self.setRandomNumber()
        self.guessedNumber = False
    
    def setRandomNumber(self):
        return random.choice([1,2,3,4,5,6,7,8,9,10])
    
    def getRandomNumber(self):
        return self.number
    
    def guessNumber(self):
        self.guessedNumber = input('guess number:')
        