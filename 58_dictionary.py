# 5:10:54
# dictionary

cities_in_F = {'New York': 32, 'Boston': 75, 'Los Angeles':100, 'Chicago':50}
print(cities_in_F)

cities_in_C = {key: round((value-32)*(5/9)) for (key,value) in cities_in_F.items()}
print(cities_in_C)

# ------------------------

weather = {'New York': 'snowing', 'Boston': "sunny", 'Los Angeles': "sunny", "Chicago":"cloudy"}
print(weather)

sunnny_weather = {key: value for (key, value) in weather.items() if value == "sunny"}
print(sunnny_weather)


# ------------------------

cities1 = {'New York': 32, 'Boston': 75, 'Los Angeles':100, 'Chicago':50}
print(cities1)

desc_cities1 = {key: ("WARM" if value >= 40 else "COLD") for (key, value) in cities1.items()}
print(desc_cities1)


# ------------------------
def check_temp(value):
    if value >= 70:
        return "HOT"
    elif 69 >= value >= 40:
        return "WARM"
    else:
        return "COLD"

cities2 = {'New York': 32, 'Boston': 75, 'Los Angeles':100, 'Chicago':50}
print(cities2)

desc_cities2 = {key: check_temp(value) for (key,value) in cities2.items()}
print(desc_cities2)