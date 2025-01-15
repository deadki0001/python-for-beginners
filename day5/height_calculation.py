# You are going to write a program that calculates the average student height from a list of heights.

# eg student_heights = [180, 124, 165, 173, 189, 169, 146]

# The average height can be calculated by adding all the heights together and dividing by the total number of heights.

# Don't change the code below

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)  

total_height = 0
number_of_students = 0

for height in student_heights:
    total_height += height
print(total_height)    

for student in student_heights:
    number_of_students += 1
print(number_of_students)    