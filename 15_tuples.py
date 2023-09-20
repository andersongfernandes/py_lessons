#tuple = collection which is ordered and unchangeable
#           used to group together related data

student = ("Anderson", 50, "male")

print(student.count("Anderson"))
print(student.index("male"))

for x in student:
    print(x)

if "Anderson" in student:
    print ("Anderson is here")