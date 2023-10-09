# 4:53:23
# map (function, iterable)

store = [("shirt",20.00),("pants",25.00),("jackets",50.00),("socks",0.00)]

exchange = 0.85
to_euros = lambda data: (data[0], round(data[1]*exchange,2)) # it is necessary to find a method to display the response as a float with 2 decimals

store_to_dollars = list(map(to_euros, store))

print(store_to_dollars)