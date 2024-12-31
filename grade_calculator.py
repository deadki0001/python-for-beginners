# A class has two tests worth 25 points each along with a main exam worth 50 points.
# For a student to pass the class, they must obtain at least 25 points in the main exam
# The overall score of at least 50 points is required to pass.
# If a students total score is less than 50 or they obtain less than 25 points in the main exam, they should recieve a grade of fail.

# Otherwise Grade as follows:
# If they get more than 80, they get a "Distinction Grade"
# If they get less than 80 but more than 60, they get a "Credit" grade.
# If they get less than 60, they get a "Pass" Grade.

# Write a program that prompts the user to enter their points for both tests and the main exam and convets the values to intergers.
# The Program should first check if the points enteredd for the tests and main exam are valid.
# If any of the test scores are not between 0 and 25 or the main exam score is not between 0 and 50, the program should display an error.
# Otherwise the program should display the total points and grade.

import sys

try:
    user_input = int(input("Kindly enter your score received in test1: "))
    user_input2 = int(input("Kindly enter your score received in test2: "))
except ValueError:
      print("Please enter a valid interger/number...")

semster_marks = user_input + user_input2

if semster_marks < 24:
    print(f"You have failed, there is no need for you to continue entering further grades...{semster_marks}")
    sys.exit()
else:
    print(f"Well done on receiving a passing score for the semester {semster_marks} points out of 50, continue to enter your exam mark next.")

try:
    user_input3 = int(input("Kindly enter your score received in the exam: "))
except ValueError:
      print("Please enter a valid integer/number...")

total_points = user_input3 + semster_marks 

semester_grade = total_points / 100 * 100

if user_input3 >= 25:
     print(f"Congratulations - You have passed the Module, your total points for the semester was {total_points} out of 100 and your pass percentage = {semester_grade}%")
else:
     print("Good Effort, Please work harder next semester")     

if semester_grade >= 80:
    print("You have been awareded a distinction")
elif 60 < semester_grade <= 79:
    print("You have been awareded Credit")
else:
     print("We look forward to seeing you next year")




     


