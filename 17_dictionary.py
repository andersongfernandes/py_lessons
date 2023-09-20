# time code = 1:40:05
# dictionary: collectio com par chave:valor

capitals = {'USA': 'Washington DC', 'India':'New Delhi', 'China':'Beijing', 'Russia':'Moscow'}

print(capitals.get('Russia'))
print(capitals.get('Germany'))
print(capitals.keys())
print(capitals.values())
print(capitals.items())

capitals.update({'Germany':'Berlin'})
print(capitals)

capitals.update({'USA':'Las Vegas'})
print(capitals)

capitals.pop('China')
print(capitals)

capitals.clear()
print(capitals)
