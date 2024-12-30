import random

user_wins = 0
computer_wins = 0

options = ['rock', 'paper', 'scissors']
# options[0, 1, 2]

while True:
    user_input = input("Choose Rock, Paper or Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, sissors: 2
    computer_picks = options[random_number]
    print('Computer chose', computer_picks + '.')

    if user_input == 'rock' and computer_picks == 'scissors':
        print("You have won!")
        

    elif user_input == 'scissors' and computer_picks == 'paper':   
        print("You have won!")
        

    elif user_input == 'paper' and computer_picks == 'rock':
        print("You have won!")
         
    else:
        print('You lose!')
            

print("Good Game!")               
