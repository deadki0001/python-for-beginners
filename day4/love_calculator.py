# The Love Calculator

# Hints
# Use the lower function
# Use the Count Function

# For Love Scores (Less than 10) or (Greater than 90), the message should be: 
# "Your score is x, you go together like Coke and Mentos"

# For Love Scores (Less than 40 and 40) , the message should be: 
# "Your score is y, you are alright together."

# Otherwise, the message will be their score. e.g.:
# "Your score is z, you are not compatibile."

# Example names
# Angela Yu
# Jack Bauer

# Check for number of times TRUE
# T occurs 0
# R occurs 1
# U occurs 2
# E occurs 2
# Total = 5

# Check for number of times LOVE
# L occurs 1 time
# O occurs 0 times
# V occurs 0 times
# E occurs 2 times
# Total = 3



print("Welcome to the Love Calculator!")
name1 = input("What is your Name? \n").lower()
name2 = input("What is your Name? \n").lower()



combined_name = name1 + name2
lower_case_name = combined_name.lower()

t = lower_case_name.count("t")
r = lower_case_name.count("r")
u = lower_case_name.count("u")
e = lower_case_name.count("e")

true = t + r + u + e 

l = lower_case_name.count("l")
o = lower_case_name.count("o")
v = lower_case_name.count("v")
e = lower_case_name.count("e")

love = l + o + v + e

love_score = int(str(true) + str(love))
             

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like Coke and Mentos")
elif (love_score >= 40) and (love_score <= 50):
    print(f"Your score is {love_score}, you are alright together")
else: 
    print(f"Your score is {love_score}, you are not compatibile.")
