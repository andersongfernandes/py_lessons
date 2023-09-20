# time code 1:04:04
# while loop

#solucao 1
name = ""

while len(name) == 0 :
    name = input("Whats your name?")

print("Solucao 1 para "+name)

#solucao 2
name = None

while not name :
    name = input("Whats your name?")

print("Solucao 2 para "+name)