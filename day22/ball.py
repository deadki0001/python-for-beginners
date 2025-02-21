from turtle import Turtle
import random

HEIGHT = 0.5
WIDTH = 0.5

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=HEIGHT, stretch_wid=WIDTH)
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1

    def move(self):
        ball_x_cor = self.xcor() + self.x_move   
        ball_y_cor = self.ycor() + self.y_move     
        self.goto(ball_x_cor, ball_y_cor)

    def bounce_y(self):
        self.y_move *= -1
        self.ball_speed *= 0.9

    def bounce_x(self):
        self.x_move *= -1        
        self.ball_speed *= 0.9
        
    def reset_position(self):
        self.goto(0, 0)
        self.ball_speed = 0.1
        self.bounce_x()