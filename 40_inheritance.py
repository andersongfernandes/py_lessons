# time code 3:48:56
# POOP python object oriented programming

class Animal:

    alive = True

    def eat(self):
        print("This animal is eatting")

    def slumber(self):
        print("This animal is sleeping")

class Rabbit(Animal):
    def run(self):
        print("This rabbit is running")

class Fish(Animal):
    def swin(self):
        print("This fish is swimming")

class Hawk(Animal):
    def fly(self):
        print("This hawk is flying")


rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

rabbit.sleep()
fish.eat()
fish.swin()
hawk.fly()