from turtle import Turtle as t, Screen
import random

tim = t()

color = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]
tim.pensize(width=15)
tim.speed(speed="fastest")

for _ in range(1000):
    tim.color(random.choice(color))
    tim.forward(30)
    tim.setheading(random.choice(directions))




screen = Screen()
screen.exitonclick()

# Tuples are ordered
# my_tuple = (1, 3, 8)
# tuples are immutable - they cannot be changed like lists

# Creating a list that stays constant - and you dont want anyone to change the inputs.
# list(my_tuple) can be converted as simple as this