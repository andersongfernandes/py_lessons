# timecode 2:09:41
# scope - region where the variable is recognized

name = "Anderson" # global scope (available inside and outside function)

def display_name():
    name = "Code" # local scope (available only inside function)
    print(name)

display_name()
print(name)