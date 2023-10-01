# time code 2:36:46
# exception

try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator
except ZeroDivisionError as e:
    print(e)
    print("It´s not possible division by zero")
except ValueError as e:
    print(e)
    print("Enter a number, plz.")
except Exception as e:
    print("Something went wrong: "+e)
else:
    print(result)
finally:
    print("This will always execute!")