# 5:04:55
# list comprehension

squares1 = []
for i in range(1,11):
    squares1.append(i * i)
print(squares1)

squares2 = [i * i for i in range(1,11)]
print(squares2)

# ----------------------------

students = [100,90,80,70,60,50,40,30,0]
print(students)

passed_students1 = list(filter(lambda x: x>= 60, students))
print(passed_students1)

passed_students2 = [i for i in students if i>=60]
print(passed_students2)

passed_students3 = [i if i>=60 else "failed" for i in students ]
print(passed_students3)
