# Create flavors 

flavours = ["Espresso", "Latte", "Cappuccino"]

# Ingriedients

ingredients = {
    "Espresso"  : {"water": 50, "coffee": 18, "milk": 0},
    "Latte"     : {"water": 200, "coffee": 24, "milk": 150},
    "Cappuccino": {"water": 250, "coffee": 24, "milk": 100},
}


prices = {
    "Espresso": 1.50,
    "Latte": 2.50,
    "Cappuccino": 3.00,
    }

# Coin Operated Coffee Machine

coins = {
    "penny": 0.01,
    "dimes": 0.10,
    "nickels": 0.05,
    "quarter": 0.25,
    }

# Program requirements

Water = 300
Milk = 200
Coffee = 100
Money = 0

def report():
    """Lists Resources in Coffee Machine"""
    print(f"Water: {Water}ml")
    print(f"Milk: {Milk}ml")
    print(f"Coffee: {Coffee}g")
    print(f"Money: ${Money:.2f}")

# 1.) Print Reports 
# 2.) Are the resources sufficient
# 3.) Process Coins
# 4.) Checks if transcation is successful
# 5.) Makes the coffee


def check_resouces(drink):
    """Checks if there are enough resources for the selected drink"""
    global Water, Milk, Coffee
    needs = ingredients[drink]

    if Water < needs["water"]:
        print(f"Not enough water! You need at least {needs['water']}ml.")
        return False        

    if Coffee < needs["coffee"]:
        print(f"Not enough coffee! You need at least {needs['coffee']}g.")
        return False

    if Milk < needs["milk"]:
        print(f"Not enough milk! You need at least {needs['milk']}ml.")
        return False

    return True    

def process_coins():
    """Prompts the user to insert coins and returns the total amount inserted."""
    print("Please insert coints")
    total = 0
    total += int(input("How many Quarters? ")) * coins["quarter"]
    total += int(input("How many Dimes? ")) * coins["dimes"]  
    total += int(input("How many Nickels? ")) * coins["nickels"]    
    total += int(input("How many Penny? ")) * coins["penny"]   

    return total


def make_coffee(drink):
    """Handles coffee making process including checking resources, processing payment, and dispensing coffee."""
    global Water, Coffee, Milk, Money

    cost = prices[drink]

    if not check_resouces(drink):
        return
    
    inserted_money = process_coins()

    if inserted_money < cost:
        print(f"Sorry, ${inserted_money:.2f} is not enough for a {drink}. Refunding money.")
        return

    # Deduct ingredients
    needs = ingredients[drink]
    Water -= needs["water"]
    Coffee -= needs["coffee"]
    Milk -= needs["milk"]


    # Update machine money
    Money += cost                

    # Give change if needed
    change = inserted_money - cost
    print(f"Here is your {drink}! ☕ Enjoy!")
    if change > 0:
        print(f"Here is your change: ${change:.2f}")

# Main program Loop

while True:
    request = input("What would you like? (espresso/latte/cappuccino/report/exit): ").strip().capitalize()

    if request == "Report":
        report()
    elif request in prices:
        make_coffee(request)
    elif request == "Exit":
        print("Goodbye! ☕")
        break
    else:
        print("Invalid input. Please enter espresso, latte, cappuccino, report, or exit.")


# My old code        

# request = input("What would you like?: (espresso/latte/cappuccino): ") 
# if request == "report":
#     report()

# # buying an espresso    
# elif request == "espresso":
#     Money = float(input("Please Insert Coins: "))     

#     if Money >= 1.50: 
#         if Coffee >= 24: 
#             if Water >= 50:
#                 Water -= 50 
#                 Coffee -= 18
#                 print("Here is your Espresso! ☕")           
#                 change = Money - 1.50
#                 if change > 0:
#                     print(f"Here is your change: ${change:.2f}")  
#             else:
#                 print(f"You only have {Water}ml of water left, please add water before we can dispense the Espresso")   
                     
#         else:
#             print(f"You only have {Coffee}g of coffee left, please add more beans to the machine")
                          
#     else:
#         print("You need to add more coins to get an Espresso.")       

   
     

# # buying a latte 
# elif request == "latte":
#     Money = float(input("Please Insert Coins: "))     

#     if Money >= 2.50: 
#         if Milk >= 160:
#             if Coffee >= 25: 
#                 if Water >= 50:
#                     Water -= 100 
#                     Coffee -= 24
#                     Milk -= 150
#                     print("Here is your Latte! ☕")           
#                     change = Money - 2.50
#                     if change > 0:
#                         print(f"Here is your change: ${change:.2f}")      
            
#                 else:
#                     print(f"You only have {Water}ml of water left, please add water before we can dispense the Latte")   
                        
#             else:
#                 print(f"You only have {Coffee}g of coffee left, please add more beans to the machine")

#         else:
#             print(f"You only have {Milk}ml of Milk left, please add Milk before we can dispense the Latte")                       
                            
#     else:
#         print("You need to add more coins to get an Espresso.")

# # buying a Cappuccino 
# elif request == "cappuccino":
#     Money = float(input("Please Insert Coins: "))     

#     if Money >= 3.00: 
#         if Milk >= 160:
#             if Coffee >= 25: 
#                 if Water >= 50:
#                     Water -= 250 
#                     Coffee -= 24
#                     Milk -= 100
#                     print("Here is your Cappuccino! ☕")           
#                     change = Money - 3.00
#                     if change > 0:
#                         print(f"Here is your change: ${change:.2f}")      
            
#                 else:
#                     print(f"You only have {Water}ml of water left, please add water before we can dispense the Latte")   
                        
#             else:
#                 print(f"You only have {Coffee}g of coffee left, please add more beans to the machine")

#         else:
#             print(f"You only have {Milk}ml of Milk left, please add Milk before we can dispense the Latte")                       
                            
#     else:
#         print("You need to add more coins to get an Espresso.")       

# report()

