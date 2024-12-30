name = input("Enter your name Player1: ")
print("Welcome", name, "to this text based adventure series")

player_type = input("Please select your class, are you a Mage, Warrior or Thief? ").lower()

print(name, 'The bold and fierce', player_type, 'wise choice - lets begin')

while True:

    answer1 = input("You emerge in a grey shrouded village, the moonlight beams across a path for you, do you go left or right? ").lower()
    if answer1 == 'left':
        print('You have stumbled upon a chest, do you open it? or continue on the path? Type open to open the Chest or walk to continue on the path ')

    elif answer1 == "open":
        print("You have picked up a wooden sword, that causes 2+ damage")

    elif answer1 == "walk":
        print("You may regret not opening the chest, what lies beyond needs equipment, are you sure you want to walk by the chest? ")

    elif answer1 == 'right': 
        print('You have fallen into a hole, please restart your journey.')   
        break
    answer2 = input("Answer 'Yes', to walk by... or 'open' to open the chest ").lower()

    if answer2 == "yes":
        print('Thats the wrong answer buddy, open the chest')
        continue
    elif answer2 == "open":
            print("You have picked up a wooden sword, that causes 2+ damage")
            print("To be continued - Anoos")
            break
    else:
        print('You have lost the game, by typing shit')


















# while True:

#     user_input = input("Would you like to play a game?, press 'q' to quit ").lower()
#     if user_input == "yes": 
#         print("You very own adventure is about to begin")
#     elif user_input == "q":
#         print("See you next time!")
#         break    
#     else:
#         print("Invalid input, type 'yes' to begin or 'q' to quit")
            
        