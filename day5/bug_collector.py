# A bug collector collects bugs every day for five days
# Write a program that keeps running total of the number of bugs collected during the five days
# The loop should ask for the total number of bugs collected each day
# When the loop is finished it should display the total number of bugs collected

collected_bugs = 0

days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

for day in days_of_week:
    daily_bugs = int(input(f"How many bugs did you collect this {day}?: "))
    collected_bugs += daily_bugs

print(f"Total number of bugs collected over the week: {collected_bugs}")


    # bugs[number] = int(bugs[number])
    # if collected_bugs < number:
    #     collected_bugs += number
    #     print(bugs)  

# userInput = int(input("How many bugs have you collected today?: "))

# for bug in bugs:
#     collected_bugs += bug

# print(userInput)
