# You are going to write a program that calculates the highest score from a list of scores.
# e.g: student_scores = [78 65 89 86 55 91 64 89]

# You are not allowed to use the min or max functions

# You must use the output words below: The highest score in class is: x

# Dont change the code below
student_scores = input("Input a list of student scores: ").split()

for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

# Write your code below this row

# Example Input:
# 78 65 89 55 91 64 89

max_score = 0

for score in student_scores:
    if score > max_score:
        max_score = score      

print(f"The highest score in the class is: {max_score}")