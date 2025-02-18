from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

# Screen Behavior

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0) 


game_start = Snake()
food = Food()
score = Score()

# Control Movements
screen.listen()
screen.onkey(game_start.up, "Up")
screen.onkey(game_start.left, "Left")
screen.onkey(game_start.down, "Down")
screen.onkey(game_start.right, "Right")
# screen.onkey(game_start.r , "Restart")


game_is_on = True

while game_is_on:
    screen.update()    
    time.sleep(0.1)  
    game_start.move()  

    # Detect collision with food
    if game_start.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        game_start.extend() 

    # Detect Collision with wall.
    if game_start.head.xcor() > 280:
        score.game_over()
        game_is_on = False
    elif game_start.head.xcor() < -280:
        score.game_over()
        game_is_on = False        
    elif game_start.head.ycor() > 280:
        score.game_over()
        game_is_on = False     
    elif game_start.head.ycor() < -280:
        score.game_over()
        game_is_on = False

    #   Detection with Tail   
    #   If head collides with any segment in the tail:    
    for segment in game_start.segments[1:]:
        if game_start.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()                     



screen.exitonclick()














