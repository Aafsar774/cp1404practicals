import random

from prac_09.car import Car
class UnreliableCar(Car):
    def __init__(self, name="", fuel=0, reliability= 100.0):
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        return f"{self.name} has fuel: {self.fuel}L reliability {self.reliability}% and drove {self.drive(100)} km"

    def drive(self, distance):
        random_number = random.randrange(0, 100)
        if random_number < self.reliability:
            return super().drive(distance)
        return 0
