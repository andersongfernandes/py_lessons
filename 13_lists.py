# timecode 1:17:10
# list = used to store multiple itens in a single variable

food = ["pizza", "hamburger", "hotdog", "spaghetti", "pudding"]
print(food)
print(food[1])

#replace the value of specific element
food[0] = "sushi"
print (food)

for x in food:
    print(x)

#add a new element in the end
food.append("ice cream")
print(food)

#delete a specific element
x = "hot dog"
if x in food: #check previourly to get integrity
    food.remove(x)
    print(food)

#delete the last element
food.pop()
print(food)

#insert a new element ia a specific position without delete any others element
food.insert(0, "cake")
print(food)

#get a alphabetic sorted list
food.sort()
print(food)

#erase all elements
food.clear()
print(food)