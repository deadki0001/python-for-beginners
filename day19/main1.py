# When a program has the requirement,
# Of having interactions with keys on a keyboard, you need to use an event listener.

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

screen.listen()

def move_forward():
    tim.forward(10)

def move_backword():
    tim.forward(-10)

def move_counter_clockwise():
    tim.left(45)    

def move_clockwise():
    tim.right(90)        

def clear_screen():
    tim.clear()   
    tim.penup()  
    tim.home()
    tim.pendown()      

#  This is a Higher Order Function
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backword)
screen.onkey(key="a", fun=move_counter_clockwise)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()