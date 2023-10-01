# timecode 4:19:12
# pass objects like arguments

class Car:
    color = None

class Motorcycle:
    color = None

def change_color(vehicle, color):
    vehicle.color = color

car1 = Car()
car2 = Car()
bike1 = Motorcycle()

change_color(car1,"blue")
change_color(bike1,"orange")

print(car1.color)
print(car2.color)
print(bike1.color)