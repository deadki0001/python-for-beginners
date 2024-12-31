# Sales Commission

# Create a variable to control the loop
keep_going = 'y'

# Calculate a series of commissions.
while keep_going == 'y':
    # Get a salesperon's sales and comission rate.
    sales = float(input('Enter the amount of sales: '))
    comm_rate = float(input('Enter the commission rate: '))

    # Calculate the commission
    commission = sales * comm_rate

    # Display the commission.
    print(f'The commission is ${commission:,.2f}.')

    # See if the user wants to do another one.
    keep_going = input('Do you want to calculate another ' + 'comission (Enter y for yes): ')
