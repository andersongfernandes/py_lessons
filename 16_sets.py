# set = collectio which is unordered, unindexed. No duplicate values.

utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cup", "knife"}

# add a new element. it is added at position 0
# utensils.add("napkin")
# print(utensils)

# delete a specific element - it is important check if the set contains the element
# x="forks"
# if x in utensils:
#     utensils.remove(x)
#     print(utensils)
    
# y="fork"
# if x in utensils:
#     utensils.remove(y)
#     print(utensils)

# delete all elements
# utensils.clear()
# print(utensils)

# pay attention: results are different if use sets in each position of update
# dishes.update(utensils)
# print(utensils)

# utensils.update(dishes)
# print(utensils)

# get the elements which are in both sets. there is no difference the position of sets in operation
# union_dinner_table1 = utensils.union(dishes)
# print(union_dinner_table1)
# union_dinner_table2 = dishes.union(utensils)
# print(union_dinner_table2)


print(dishes)
print(utensils)

# get the element which are in one set and are not in the other one
difference_dishes_utensils = dishes.difference(utensils)
print(difference_dishes_utensils)
difference_utensils_dishes = utensils.difference(dishes)
print(difference_utensils_dishes)

# get the element which are in both sets
intersect_dishes_utensils = dishes.intersection(utensils)
print(intersect_dishes_utensils)