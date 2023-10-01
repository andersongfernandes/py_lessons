# time code 2:51:01
# handle file

newText2 = "Yoooooo\nThis is some text\nHave a good one!!\n"
appendText2 = "A snippet appended by code."

# with open('test2.txt', 'w') as file: #'w' is used to edit and overwrite the file text2 with the content of var newText2
#     file.write(newText2)

with open('test2.txt','a') as file: #'a' is used to append content to an existing text content 
    file.write(appendText2)