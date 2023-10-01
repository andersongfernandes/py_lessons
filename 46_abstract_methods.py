# timecode 4:12:11
# abstract functions - prevents a user to creating on object of class and compels a user to override the methods in a child methods

from abc import ABC, abstractclassmethod

class Vehicle(ABC):

    @abstractclassmethod
    def go(self):
        pass

    @abstractclassmethod
    def stop(self):
        pass

class Car(Vehicle):

    def go(self):
        print("You drive the car")

    def stop(self):
        print("You stop the car")


class Motorcycle(Vehicle):

    def go(self):
        print("You drive the motocycle")

    def stop(self):
        print("You stop the motocycle")



car = Car()
motorcycle = Motorcycle()
car.go()
motorcycle.stop()