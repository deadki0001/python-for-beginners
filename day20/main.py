from turtle import Screen, Turtle
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)    

game_start = Snake()

# Control Movements
screen.listen()
screen.onkey(game_start.up, "Up")
screen.onkey(game_start.left, "Left")
screen.onkey(game_start.down, "Down")
screen.onkey(game_start.right, "Right")


game_is_on = True

while game_is_on:
    screen.update()    
    time.sleep(0.1)  

    game_start.move()  



screen.exitonclick()














