# Object State and instances

from turtle import Turtle, Screen
import random
# Screen logic
is_race_on = False
screen = Screen()
                 #Y           #X Axis    
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="Who will win the Race? Enter a color: ")
colors = ["red", "orange", "yellow", "blue", "green", "purple"]
y_pos = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle") # These are seprate instances of the turtle objects
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230 , y=y_pos[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:    
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else: 
                print(f"You've lost! The {winning_color} turtle is the winner!")    
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

# tom = Turtle(shape="turtle") # These are seprate instances of the turtle objects
# tom.color("orange")
# tom.penup()
# tom.goto(x=-230 , y=-80)

# lee = Turtle(shape="turtle") # These are seprate instances of the turtle objects
# lee.color("yellow")
# lee.penup()
# lee.goto(x=-230 , y=-60)

# ricky = Turtle(shape="turtle") # These are seprate instances of the turtle objects
# ricky.color("green")
# ricky.penup()
# ricky.goto(x=-230 , y=-40)

# goku = Turtle(shape="turtle") # These are seprate instances of the turtle objects
# goku.color("blue")
# goku.penup()
# goku.goto(x=-230 , y=-20)

# annie = Turtle(shape="turtle") # These are seprate instances of the turtle objects
# annie.color("purple")
# annie.penup()
# annie.goto(x=-230 , y=0)

# 

screen.exitonclick()