print("Welcome to the Tip Calculator!")

user_input = float(input("What was the total bill? "))
print(f"${user_input}")
user_input2 = float(input("How much tip would you like to give? 10%, 12%, or 15%? "))
if user_input2 == 10:
    print(f"Each person should pay ${user_input * 0.10}") 
elif user_input2 == 12:  
  twelve_percent = print(f"Each person should pay ${user_input * 0.12}")     
elif user_input2 == 15:  
    fifteen_percent = print(f"Each person should pay ${user_input * 0.15}")    
user_input3 = float(input("How many people should share the bill? "))
print(f"Each person should pay: ${user_input3 / user_input + user_input:.2f}")




                
                