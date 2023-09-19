# time_code = 41.05
# slicing: create substring by extracting elements from another string
# indexing[] or slice()
# start:stop:step

#INDEX
name = "Anderson Fernandes"

first_name = name [:8]
last_name = name [9:]
funky_name = name [::2]
reversed_name = name[::-1]

print(first_name)
print(last_name)
print(funky_name)
print(reversed_name)

#SLICE
website = "http://google.com"
slice = slice(7,-4)

print(slice)
print(website[slice])