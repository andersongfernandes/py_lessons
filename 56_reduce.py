# 5:00:11
# reduce

import functools

letters = ["H", "E", "L", "L", "O"]
conc = lambda x,y: x+y
word = functools.reduce(conc,letters)
print(word)

numbers = [5,4,3,2,1]
factFunct = lambda x,y: x*y
fact = functools.reduce(factFunct, numbers)
print(fact)

