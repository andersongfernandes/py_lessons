# time code 4:41:07
# lambda function
# lambda parameters:expression

double = lambda x: x*2
multiply = lambda x,y: x * y
add = lambda x,y: x + y
full_name = lambda first_name, last_name: first_name+" "+last_name
age_check = lambda age: True if age >= 18 else False

print(double(3))
print(multiply(2,4))
print(add(2,4))
print(full_name("A","B"))
print(age_check(17))
print(age_check(18))
