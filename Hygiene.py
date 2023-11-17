class Hygiene:
    def __init__(self):
        self.duration = 12
    
    def poop(self):
        if self.duration > 0:
            self.duration -= 1
            return -10
        else:
            return 0

    def wash(self):
        if self.duration < 12:
            self.duration += 1
            return 10
        else:
            return 0