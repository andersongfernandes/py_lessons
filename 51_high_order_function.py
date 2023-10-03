# time code 4:35:21
# high_order_function - accepts a function as an argument

def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def hello(func):
    text = func("HEllo")
    return(text)

finalText = hello(quiet)
print(finalText)

finalText = hello(loud)
print(finalText)


# high_order_function - returns a function as an response

def divisor(x):
    def dividend(y):
        return y/x
    return dividend

divide = divisor(2)
print(divide(10))