# Write a program that asks the user to enter the number of times they have run around a racetrack.
# Use a loop to prompt them to enter the lap time for each of their laps.
# When the loop finishes, the program should display the time of their fastest lap.
# The time of the slowest lap.
# Their lap time average.


number_of_laps = int(input("How many times have you run around the racetrack?: "))
lap_times = []

for lap in range(1, number_of_laps + 1):
    time_taken = int(input(f"How many minutes did it take you to complete this {lap} track?: "))   
    lap_times.append(time_taken)

max_time = max(lap_times)
min_time = min(lap_times)
average_lap_time = max_time / min_time

print(f"Your Fasted time was {max_time} and your slowest lap was {min_time} and your lap average was {average_lap_time}")



# print(f"You have ran a total of {laps}! laps")
# lap_time = int(input("How many minutes did it take you to cycle through the lap? :"))