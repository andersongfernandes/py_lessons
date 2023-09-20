# time code 1:13:05
# nested loop

rows = int(input("How many rows? "))
column = int(input("How many columns? "))
symbol = input("Choose a symbol do use: ")

for i in range (rows):
    for j in range (column):
        print(symbol, end="")
    print()