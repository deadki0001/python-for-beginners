# A bug collector collects bugs every day for five days.
# Write a program that keeps running a total of the number of bugs collected during the 5 days.
# The loop should ask for the number of bugs collected for each day
# When the loop is finished the program should display the total number of bugs collected.

days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
total_number_of_bugs = 0
day_index = 0

# Use a while loop with day names
while day_index < len(days_of_week):
    day = days_of_week[day_index]
    bugs = int(input(f"How many bugs have you collected this {day}?: "))
    total_number_of_bugs += bugs
    day_index += 1

print(f"You have collected a total of {total_number_of_bugs} bugs this week. Well done!")
