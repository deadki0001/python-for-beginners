import random
import os

# Goal add up cards to the largest number without going over 21

# If cards in hand add up to more than 21 its called a bust - You lose straight away

# Cards 2 - 10 count as face value

# Cards Jack Queen and King Count as 10

# Card ACE can count as 1 or 11 towards your total 

# Draws can be possible

### Step 1 - Get Random Cards to your Hand

### Step 2 - Display computers first card

### Step 3 = Type "Y" to get another card, type 'n' to pass: n

### Step 4 = Display Your Final Hand

### Step 5 = Computer plays final Hand

### Step 6 = Once you know what your doing loop the game


# Create a deal_card() function that uses the list below to *return* a random card.
# 11 is the Ace
def deal_card():
    """Returns a Random Card from the Deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card =  random.choice(cards)
    return card

def calculate_score(cards):
   """Take a list of cards and return the score calculated from the cards"""
   if sum(cards) == 21 and len(cards) == 2:
       return 0   
   return sum(cards)    

def play_game():
# Deal the user and computer 2 cards each using deal_card() AKA HINT 5
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # The score will need to be rechecked with every new card drawn and the checks need to be repeated until the game ends


    # Inside calculate_score() check for blackjack (a hand with only 2 cards: ace + 10)
    # Return 0 instead of the actual score. 0 Will represent a blackjack in our game.

    # Inside calculate_score() check for an 11 (ace). if the score is already over 21, remove the 11 and replace it with a 1.
    # You might need to looj up append() and remove()

    while not is_game_over:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"    Your cards: {user_cards}, current score; {user_score}")
        print(f"    Computers first card: {computer_cards[0]}")    

        # Create a function called calculate_score() that takes a list of cards as input and returns the score.
        # Look up the sum() function to do this

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal =  input("Type 'y' to get another card, type 'n' to pass: ")    
            if  user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True   
        # If the game has not ended, ask the user of they want to draw another card. If yes, 
        # Then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.   
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
        # Once the user is done, its time to let the computer play. 
        # The computer should keep drawing cards as long as it has a score less than 17.

    # Create a function called compare() and pass in the user_score an computer_score.
    # If the commputer and user both have the same score, then its a draw.
    # If the computer has a blackjack(0), then the user loses.
    # If the user has a blackjack (0), then the user wins. 
    # If the user_score is over 21, then the user loses.
    # If the computer_score is over 21, then the computer loses.
    # If none of the above, then the player with the highest score wins.
    def compare(user_score, computer_score):
        if user_score == computer_score:
            return "Draw"
        elif computer_score == 0:   
            return "You Lose, oppoent has Blackjack"
        elif user_score == 0:
            return "You win with a Blackjack"
        elif user_score > 21:
            return "You Bust, You Lose!"
        elif computer_score > 21:
            return "The Computer Bust, You Win!"    
        elif user_score > computer_score:
            return "You got the greater score, You Win!"  
        else:
            return "The computer got the greater score, You Lose!"            

    print(f"    Your final hand: {user_cards}, final score: {user_score}")
    print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")     
    print(compare(user_score, computer_score))

    # Ask the user if they want to restart the game. 
    # If they answer yes, clear the console and start a new game of blackjack. 

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    os.system('clear')
    play_game()