import random

print("Welcome to the PyPassword Generator! \n")

alphabet = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
    'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
    'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
    'w', 'x', 'y', 'z'
]


symbols = [
    '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', 
    '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', 
    ']', '^', '_', '`', '{', '|', '}', '~'
]

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

letters = int(input("How many letters would you like in your password?: \n"))
letter_randomization = ''.join(random.choice(alphabet) for _ in range (letters))
num_symbols = int(input("How many symbols would you like in your password?: \n"))
num_symbols_randomization = ''.join(random.choice(symbols) for _ in range(10))
number = int(input("How many numbers would you like in your password?: \n"))

letters = str(letters)
symbols = str(symbols)
number = str(number)

generated_password = [letter_randomization + num_symbols_randomization + number]


random.shuffle(generated_password)

new_password = ''.join(generated_password)
print(new_password)
