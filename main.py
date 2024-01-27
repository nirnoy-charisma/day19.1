import random
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
screen.listen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def counter_clockwise():
    new_heading=tim.heading()+10
    tim.setheading(new_heading)
    tim.forward(10)


def clockwise():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)
    tim.forward(10)


def clear_drawing():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


tim.pensize(3)

screen.onkey(key="d", fun=counter_clockwise)
screen.onkey(key="a", fun=clockwise)
screen.onkey(key="c", fun=clear_drawing)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="w", fun=move_forwards)
screen.exitonclick()
