from turtle import Turtle

WIDTH = 5
HEIGHT = 1



class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=HEIGHT, stretch_wid=WIDTH)        
        self.goto(position)


    def paddle_up(self):
        y_pos = self.ycor() + 20
        self.goto(self.xcor(), y_pos)

    def paddle_down(self): 
        y_pos = self.ycor() - 20
        self.goto(self.xcor(), y_pos)

