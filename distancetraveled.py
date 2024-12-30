# The distance a car travels down the state can be calculated as Distance = Speed x Time
# A car is travelling at 70 miles per hour. Write a program that displays

# The distance the car will travel in 6 hours
# The distance the car will travel in 10 hours
# The disntance the car will travel in 15 hours


distance = 70 * 1

user_input = int(input("How many hours have you travelled?: "))

distance_travelled = user_input * distance

print(f"The car has traveled {distance_travelled} miles, in {user_input} hours. ")

