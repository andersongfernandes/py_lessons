#time code = 58h28
#logical operators

temp = int(input("What is the temperatura outside?"))

if temp>=0 and temp<=30:
    print("The wheather is good today")
elif temp<0 or temp>30:
    print("The weather is not good today. Stay inside")
