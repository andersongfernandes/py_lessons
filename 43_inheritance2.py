# time code 4:01:50
# inheritance

class Animal:
    def eat(self):
        print("This animal is eatting")

class Rabbit(Animal):
    def eat(self):
        print("This rabbit is eatting a carrot")

rabbit = Rabbit()

rabbit.eat() #the local function overwrite the global one
