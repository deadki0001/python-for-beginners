from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

""""
--------------------
Program Requirements
--------------------
1.) Print Report.
2.) Check if resources are sufficient.
3.) Process coins.
4.) Check transaction successful.
5.) Make coffee.

"""
coffee_maker = CoffeeMaker()
coffee_maker.report()
is_on = True

money_machine = MoneyMachine()
money_machine.report()

menu = Menu()


while is_on == True:
    options = menu.get_items()
    choice = input(f"what would you like to order today?: ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()    
        money_machine.report()    
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
        



# # We need to check the report
# # This will let us know in advance if we can place certain orders
# resources = CoffeeMaker()
# resources.report()
# print(resources)

# __init__()
# # Check if resources are sufficient.

# ingredients = CoffeeMaker()
# ingredients.is_resource_sufficient()

# # Process Coins
# process_coins = MoneyMachine()
# process_coins.process_coins()
# process_coins.make_payment()
# process_coins.profit()

# # Make Coffee
# resources.make_coffee()


