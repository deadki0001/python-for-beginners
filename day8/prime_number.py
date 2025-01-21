# Prime number is a number that can only be divisible by 1 and itself

# Write your code below this line

def prime_checker(number):
    is_prime = True
    for i in range(2, number):
      if number % i == 0:
        is_prime = False
    if is_prime:  
        print("Is a Prime Number")
    else:
         print("Is not a Prime Number")  


# Write your code above this line


n = int(input("Check this number: "))
prime_checker(number=n)

# It's a prime number

# It's not a prime number