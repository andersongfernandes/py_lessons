# 4:57:34
# filter (function, interable)

store = [("shirt",20.00),("pants",25.00),("jackets",50.00),("socks",0.00)]

price_max = lambda data: data[1] <= 20.00

oullet_products = list( filter(price_max, store) )

print(oullet_products)