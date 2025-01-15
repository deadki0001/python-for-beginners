import random

rps = ["Rock", "Paper", "Scissors"]

choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: \n")

choice = int(choice)

computer = random.randint(0, 2)


if choice == 2 and computer == 1:
    print("Scissors beats Paper, You Win!, restart the game to play again")
elif choice == 1 and computer == 0:
    print("Paper beats Rock, You Win!, restart the game to play again")  
elif choice == 0 and computer == 2:
    print("Rock beats Scissors, You Win!, restart the game to play again")
elif choice == 0 and computer == 0:
    print("You have a draw - Try again")        
elif choice == 1 and computer == 1:
    print("You have a draw - Try again")  
elif choice == 2 and computer == 2:
    print("You have a draw - Try again")
elif computer == 0 and choice == 1:
    print("You win!!,  Paper beats Rock draw - Restart to play again")                      
else:
    print(f"You lose, the computer chose {computer[choice]}, which beats {choice[rps]} try again...")      

