travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]


def add_new_country(country, visits, cities):
    new_country = {}
    travel_log.append(new_country)
    new_country["country"] = country
    new_country["visits"] = visits
    new_country["cities"] = cities


print("Add data to your travel log.")

user_country = input("Country: ")
user_visits = input("Visits: ")
user_cities = input("Cities: ").split(', ')

add_new_country(user_country, user_visits, user_cities)

print(travel_log)
