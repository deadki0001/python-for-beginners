# Write a progam that asks the user to enter an Interger. 
# The program should display "Positive" if the number is greater than 0
# It should display "Negative" if the number is less than 0.
# Lastly it should display "Zero" if the number is equal to 0.
# The program should be display "Even" if the number is even, and "Odd" if the number is odd.

user_input = int(input("Enter a Integer: "))
if user_input % 2 == 0 and user_input > 0: 
    print("The number is Positive and the Number is even")
elif user_input < 0:
    print("The number is Negative")    
elif user_input == 0:
    print("The number provided is Zero, please enter another number")
else: 
    print("This is a Postive interger and the number is Odd")
