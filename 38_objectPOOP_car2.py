# time code 3:45:08
# POOP python object oriented programming

from assets.carPoop.car import Car

car_1 = Car("Chevy","Corvette",2021,"blue")
car_2 = Car("Ford","Mustang",2022,"red")

print(car_1.wheels)
print(car_2.wheels)

car_1.wheels = 2
print(car_1.wheels)
print(car_2.wheels)

# changing the class settings
print(Car.wheels)

# the local setting is over than the class one
Car.wheels = 3
print(car_1.wheels)
print(car_2.wheels)
Car.driveModel(car_1)
Car.stopModel(car_2)