from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

setup_screen = Screen()
setup_screen.setup(width=800, height=600)
setup_screen.bgcolor("black")
setup_screen.title("The Pong Game")
setup_screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()

setup_screen.listen()
setup_screen.onkey(r_paddle.paddle_up, "Up")
setup_screen.onkey(r_paddle.paddle_down, "Down")
setup_screen.onkey(l_paddle.paddle_up, "w")
setup_screen.onkey(l_paddle.paddle_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.ball_speed)
    setup_screen.update()
    ball.move()

    # Detect Collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # The ball needs to bounce_y
        ball.bounce_y()

    # Detect Collission with Paddle Object
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() > -340:
        ball.bounce_x()

    # Detect when R_Paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()


    # Detect when L_Paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()   
       


    # Scoring logic

setup_screen.exitonclick()