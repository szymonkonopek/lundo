class Bed:
    def __init__(self, duration, energyCount):
        self.duration = duration
        self.energyCount = energyCount

    def use(self):
        if self.duration > 0:
            self.duration -= 1
            return self.energyCount
        else:
            return 0