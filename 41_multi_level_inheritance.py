# time code 3:55:31
# multi-level inheritance

class Organism:
    alive = True

class Animal(Organism):
    def eat(self):
        print("This aninal is eatting")

class Dog (Animal):
    def bark(self):
        print("This dog is barting")


dog = Dog()
print(dog.alive)
dog.eat()