# timecode 2:13:25
# args

def add1(*arg):
    sum = 0
    for i in arg:
        sum += i
    return sum

print(add1(1,3,8))
print(add1(2,4))

def add2(*stuff):
    sum = 0
    stuff = list(stuff)
    stuff[0] = 0
    for i in stuff:
        sum += i
    return sum

print(add2(1,2,3,4,5,6))