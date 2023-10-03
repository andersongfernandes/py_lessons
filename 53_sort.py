# 4:45:45
# sort function with iterables, method with lists


# sort lists using function
students = ["Squidward", "Sandy", "Patrick", "Spongebob", "Mr. Krabs"]

students.sort()
for i in students:
    print(i)

students.sort(reverse=True)
for i in students:
    print(i)

# sort tuples using method
students = ("Squidward", "Sandy", "Patrick", "Spongebob", "Mr. Krabs")

sorted_students = sorted(students)
for i in sorted_students:
    print(i)

sorted_students = sorted(students, reverse=True)
for i in sorted_students:
    print(i)


# sort lists of tuples using function
students = [("Squidward", "F", 60), 
            ("Sandy", "A", 33), 
            ("Patrick", "D", 36), 
            ("Spongebob", "B", 20), 
            ("Mr. Krab", "C", 78)]


#sort by the 1rs column by default
students.sort()
for i in students:
    print(i)

#sort by the 2nd column
grade = lambda grades:grades[1]
students.sort(key=grade)
for i in students:
    print(i)

#sort reversed by the 3nd column
grade = lambda grades:grades[2]
students.sort(key=grade, reverse=True)
for i in students:
    print(i)

# sort tuples of tuples using methods
students = (("Squidward", "F", 60), 
            ("Sandy", "A", 33), 
            ("Patrick", "D", 36), 
            ("Spongebob", "B", 20), 
            ("Mr. Krab", "C", 78))

#sort by the 1rs column
grade = lambda grades:grades[0]
sorted_students = sorted(students,key=grade)

for i in sorted_students:
    print(i)

#sort by the 2nd column
grade = lambda grades:grades[1]
sorted_students = sorted(students,key=grade,reverse=True)

for i in sorted_students:
    print(i)

#sort by the 2nd column
grade = lambda grades:grades[2]
sorted_students = sorted(students,key=grade,reverse=False)

for i in sorted_students:
    print(i)
