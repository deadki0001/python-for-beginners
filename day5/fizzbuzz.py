# Your program should print each number from 1 to 100 in turn.

# When the number is divisble by 3 then instead of printing the number it should print "Fizz".

# When the number is divisble by 5, then instead of printing the number it should print "Buzz"

# And if the number is both divisble by both 3 and 5 e.g 15 then instead of the nbumber it should print FizzBuzz.

for num in range(1, 101):

    if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")        
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz") 
    else:    
        print(num)
