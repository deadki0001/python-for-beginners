#################################################
# CREATING VARIABLES FOR PIZZA PROGRAM          # 
#################################################

final_bill = 0

small_pizza = 15

medium_pizza = 20

large_pizza = 25

pepperoni_small = +2

pepperoni_medium_large = +3

extra_cheese = +1

##################################################
# Creating Pizza Sizes & Yes or No Promts        #
##################################################

s = "s"

m = "m"

l = "l"

y = "y"

n = "n"

#################################################
#         MAIN LOGIC                            #
#################################################

print("Welcome to Python Pizza Deliveries")
 
# Obtain order

size = user_input = input("What size pizza do you want? S, M, L: ").lower()

if user_input == s:
    final_bill += small_pizza
    print(f"Added small pizza: ${small_pizza}")    
elif user_input == m:
    final_bill += medium_pizza
    print(f"Added medium pizza: ${medium_pizza}")    
elif user_input == l:
    final_bill += large_pizza
    print(f"Added large pizza: ${large_pizza}")    
else:
    print("Please select a size between, S, M or L")
    exit()            

# Now add the pepperoni
pepperoni = input("Would you like pepperoni with your order? Y / N: ").lower()

if pepperoni == "y":
    if size == "s":
        final_bill += pepperoni_small
        print(f"Added small pepperoni: ${pepperoni_small}")    
    else:  # Medium or large pizzas
        final_bill += pepperoni_medium_large
        print(f"Added medium/large pepperoni: ${pepperoni_medium_large}")
elif pepperoni == "n":  # No action needed for "no"
    print("No pepperoni added.")            

# Asking user for extra cheese
cheese = input("Would you like extra cheese? Y / N: ").lower()

if cheese == "y":
    final_bill += extra_cheese
    print(f"Added extra cheese: ${extra_cheese}")

# Final output
print(f"Thank you for your order! Your total is: ${final_bill}")




#     print(f"The Charge for your Small Pizza will be ${final_bill += small_pizza}")
#     print("Would you like Pepperoni, with your order?: Y / N: ")
#     if user_input == y: 
#         print(f"The total for your order comes up to: ${small_pizza + pepperoni_small}")    
#     else:
#         print(f"Thank you for your order today, your total for today is {final_bill}")

# elif user_input == m: 
#         print(f"The Charge for your Small Pizza will be ${medium_pizza}")
#         if user_input == y: 
#             print(f"The total for your order comes up to: ${medium_pizza + pepperoni_medium_large}")    
#         else:
#             print(f"Thank you for your order today, your total for today is {final_bill}")

# elif user_input == l:
#         print(f"The Charge for your Small Pizza will be ${large_pizza}")  
#         if user_input == y: 
#             print(f"The total for your order comes up to: ${large_pizza + pepperoni_medium_large}")    
#         else:
#             print(f"Thank you for your order today, your total for today is {final_bill}")     






