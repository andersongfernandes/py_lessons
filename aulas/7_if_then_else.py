# if statement

age = int(input("How old are u?"))

if age == 100 :
    print("You are a century old!")
elif age >= 18 :
    print("You are an adult.")
elif age < 0 :
    print("You havent been born yet!")
else :
    print("You are a child!")