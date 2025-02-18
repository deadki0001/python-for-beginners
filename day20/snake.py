
from turtle import Screen, Turtle
import tkinter as tk


STARTING_POSITIONS = [((0,0)), ((-20,0)), ((-40,0))]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0



# Create Snake Body - Step 1

class Snake():

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    
    # Where new segment equals the body of the snake

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segement = Turtle("square")
            new_segement.color("white")
            new_segement.penup()
            new_segement.goto(position)
            self.segments.append(new_segement)    

        # Control Snake Movement

    def move(self):
        for seg_num in range(len(self.segments) - 1 ,0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)    

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP) 

    def down(self): 
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:      
            self.head.setheading(LEFT)

    def right(self):  
        if self.head.heading() != LEFT:   
            self.head.setheading(RIGHT)










