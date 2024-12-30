print("Welcome to the Dragonballz General Knoweldge Quiz")

playing = input("Would you like to play? ") #user input

if playing.lower() != "yes": #condition
    quit()      #built in python function to quit program

print("Awesome! Let's begin!!") 
score = 0

answer1 = input("Who is Goku's Wife? ").lower()

if answer1 == "chichi":
    print("Well done, you just earned 2 points!")
    score += 2
else:
    print("That's Incorrect - start again") 

answer2 = input("Who is the cutest DBZ character? ").lower()

if answer2 == "bulma":
    print("Well done, you just earned 2 points!")
    score += 2
else:
    print("That's Incorrect - start again") 

print("You got " + str(score) + " points!")    