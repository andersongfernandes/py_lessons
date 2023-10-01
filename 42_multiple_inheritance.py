# time code 3:58:34
# multiple inheritance

class Prey:
    def flee(self):
        print("This animal flees")

class Predator:
    def hunt(self):
        print("This animal is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

rabbit.flee()
# rabbit.predator() #error: it not define to class Rabbit
hawk.hunt()
fish.flee()
fish.hunt()

