# time code 2h34:41
# os
import os

path = "C:\\Users\\Live\\Desktop\\Importante\\Python World\\py_lessons\\29_os.py"

if os.path.exists(path):
    print("That location exists")
    if os.path.isfile(path):
        print("It is a file")
    elif os.path.isdir(path):
        print("It is a folder")
else:
    print("This location doesn`t exist!")