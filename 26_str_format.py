#   time code 2:21:19
#string format

animal = "cow"
item = "moon"
print("1. The {} jumped over {}".format(animal,item))
print("2. The {1} jumped over {0}".format(item,animal)) #positional arguments

print("3. The {what} is on {where}".format(what="book",where="table")) #keywords arguments

text = "4. The {what} is on {where}"
print(text.format(what="book",where="table"))

text = "5. The {} jumped over {}"
print(text.format(animal,item))


name = "Anderson"
print("My name is {:15}. Note the qtd of spaces".format(name))
print("My name is {:<15}. Note the qtd of spaces".format(name))
print("My name is {:>15}. Note the qtd of spaces".format(name))
print("My name is {:^15}. Note the qtd of spaces".format(name))
print("My name is {:5}. Note the qtd of spaces".format(name))


number = 1000
print("The number is {:.3f}".format(number)) #3 decimal
print("The number is {:,}".format(number)) #thousands
print("The number is {:b}".format(number)) #binary
print("The number is {:o}".format(number)) #octo
print("The number is {:X}".format(number)) #hexadecimal
print("The number is {:E}".format(number)) #cientific notation
