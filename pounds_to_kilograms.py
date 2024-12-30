# 1 pound is equilavent to 0.454 kgs.
# Write a program that asks for the user to input the mass of an object.
# The program should then calculate the mass of the object in punds then displays the mass of the object in kilograms.

one_pound = 1 
user_input = float(input('Enter the mass of an object in pounds: '))

pound_to_kgs = 0.454

converted = pound_to_kgs * one_pound

result = user_input * converted
print(f"The total converted mass {result} kg's")
