# Company total annual profit is 23% of the total sales.
# Write a program that asks the user to enter the projected amount of total sales, 
# Next ensure it displays the profit made from the amount

total_sales = float(input("Enter the Total Sales Number for the Year: ")) 
profit_margin = 0.23
total_profit_made = profit_margin * total_sales

print(f"The total profit made for the year: ${total_profit_made:.2f}")