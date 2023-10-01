# time code 2:47:29
# handle file

try:
    with open('test.txt') as file:
        print(file.read())
except FileNotFoundError:
    print ("File not found!")