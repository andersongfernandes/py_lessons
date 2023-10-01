# time code 2:58:04
# os

import os

destination = "assets/test1.txt"
source = "C:\\Users\\Live\\Downloads\\devFolder\\test1.txt"

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source, destination)
        print(source+" was moved")
except FileNotFoundError:
    print(source+" was not found")