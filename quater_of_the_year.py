# Write a program that asks the user for a month as a number between 1 and 12.
# The program should display a message indicating whether the month is in the first quarter, the second quarter, the third quater or the last quarter of the year.
# Following the guidelines:
# If the user enters a number between 1 and 3, the month is the first quarter.
# If the user enters a number between 4 and 6, the month is in the second quarter.
# If the user enters a number beetween 7 and 9, the month is in the third quarter.
# if the number is not between 1 and 12, the program should display an error.

months_in_year = {
    "1": "January" ,
    "2": "February" ,
    "3": "March" ,
    "4": "April" ,
    "5": "May" ,
    "6": "June" ,
    "7": "July" ,
    "8": "August" ,
    "9": "Septmeber" ,
    "10": "October" ,
    "11": "November",
    "12": "December"                     
}

user_input = int(input("Input a number between 1 and 12, Where 1 = January and 12 = December, this will output the Yearly Quarter: "))

if user_input == 1:
    print(months_in_year["1"], "- First Quarter of the Year")
elif user_input == 2:
    print(months_in_year["2"], "- First Quarter of the Year")   
elif user_input == 3:
    print(months_in_year["3"], "- First Quarter of the Year")       
elif user_input == 4:
    print(months_in_year["4"], "- Secolnd Quarter of the Year")    
elif user_input == 5:
    print(months_in_year["5"], "- Secolnd Quarter of the Year")   
elif user_input == 6:
    print(months_in_year["6"], "- Secolnd Quarter of the Year")   
elif user_input == 7:
    print(months_in_year["7"], "- Thrid Quarter of the Year")     
elif user_input == 8:
    print(months_in_year["8"], "- Thrid Quarter of the Year")  
elif user_input == 9:
    print(months_in_year["9"], "- Thrid Quarter of the Year")         
elif user_input == 10:
    print(months_in_year["10"], "- Fourth Quarter of the Year")            
elif user_input == 11:
    print(months_in_year["11"], "- Fourth Quarter of the Year")    
elif user_input == 12:
    print(months_in_year["12"], "- Fourth Quarter of the Year")   
else:
    print("Enter a Number between 1 & 12 to receive the yearly quarter input")                           

