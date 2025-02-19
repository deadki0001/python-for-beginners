from turtle import Turtle, Screen
from snake import Snake 
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title("My Snake Game")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
screen.update()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.down, "Down")

game_is_on = True

while game_is_on:
    screen.update()    
    time.sleep(0.3)       
    snake.move()


# Collission with food    
    if snake.head.distance(food)  < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

# collision with Wall

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()    










screen.exitonclick()





