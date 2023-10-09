# timecode 05:19:03
# zip

usernames = ["Dude", "Bro", "Mister"] #list
passwords = ("p@ssword","abc123","guest") #tuples

users = zip(usernames, passwords)

for i in users:
    print(i)

# ('Dude', 'p@ssword')
# ('Bro', 'abc123')
# ('Mister', 'guest')


users_list = list(users)

for i in users_list:
    print(i)

# ('Dude', 'p@ssword')
# ('Bro', 'abc123')
# ('Mister', 'guest')


print(type(users))
# <class 'zip'>

print(type(users_list))
# <class 'list'>


