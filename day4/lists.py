import random

names_string = input("Give me everybody's names, seperated by a comma. ")

names = names_string.split(",")

bill_payer = random.choice(names)

print(f"{bill_payer} is going to buy the meal today!")