
# capitals = {
#     "France": "Paris",
#     "Germany": "Berlin",
#     }

# # Nesting a list in a dictionary

# travel_log = {
#     "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
#     "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 8}
# }

# print(travel_log)

# Nesting Dictionay in a list

travel_log = [
    {
    "country": "France", 
     "cities_visited": ["Paris", "Lille", "Dijon"], 
     "total_visits": 12
     },
    {
    "country": "Germany", 
     "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
     "total_visits": 8
     },
]

print(travel_log)