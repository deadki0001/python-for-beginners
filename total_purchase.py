# A customer in a store is purchasing 5 items.
# Write a program that aks for the price of each item.
# The display should provide the sub-total of the sale.
# The Tax amd the final total.
# Ensure that the tax is calculated at 14 percent.


# tax = 14 * 100

prices = {
    "chips": 5.00,
    "juice":  6.00,
    "chocolate": 10.00
}

tax_rate = 0.14

user_input = input("What would you like to purchase today: ").lower()

if user_input in prices:
    subtotal = prices[user_input]

    tax = subtotal * tax_rate

    total = subtotal + tax

    print(f"{user_input.capitalize()} will cost you a Sub Total of R{subtotal:.2f}")
    print(f"Tax (14%): R{tax:.2f}")
    print(f"Total Cost: R{total:.2f}")
else:
    print("Sorry, we don't have that item.")    


