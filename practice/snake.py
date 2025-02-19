from turtle import Turtle

# TRY TO USE CONSTANTS AS MUCH AS POSSIBLE FOR LATER TWEAKS

STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
ALIGNEMNT = "center"
FONT = ('Arial', 20, 'normal')


class Snake:

    def __init__(self):
        self.segments = []  # where segments equals a block of the turtle - representing the snakes body.
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        positions = STARTING_POSITIONS # The list of positions for the snakes body    
        for position in positions:
            self.add_segment(position)

    def move(self):
        for segment_number in range(len(self.segments) -1, 0, -1):
            new_x = self.segments[segment_number -1].xcor()
            new_y = self.segments[segment_number -1].ycor()
            self.segments[segment_number].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)
  
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def down(self):  
        if self.head.heading() != UP:      
            self.head.setheading(DOWN)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)        
                

    def extend(self):    
        self.add_segment(self.segments[-1].position())