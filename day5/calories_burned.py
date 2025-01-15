# Running on a particular treadmill you burn 4.2 calories per minute.
# Write a program that uses a lopp to display the number of calories burned after 10, 15, 20, 25 and 30 minutes.

calories_per_min = 4.2

total_calories_burned = 0

mins_burned = [10, 15, 20, 25, 30]

for mins in mins_burned:
    result = mins * calories_per_min
    print(result)
