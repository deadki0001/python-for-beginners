travel_log = [
    {
    "country": "France", 
     "total_visits": 12,    
     "cities_visited": ["Paris", "Lille", "Dijon"], 
     },
    {
    "country": "Germany",
     "total_visits": 8,     
     "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
     },
]

# Write a function that will work with the following line of code

def add_new_country(country_visted, total_visits, cities_visted):
    new_country = {}
    new_country["country"] = country_visted
    new_country["total_vists"] = total_visits
    new_country["cities_visted"] = cities_visted
    travel_log.append(new_country)         


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)