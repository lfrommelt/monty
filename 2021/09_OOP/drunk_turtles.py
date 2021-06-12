from turtle import Screen, Turtle
from random import random

class DrunkTurtle(Turtle):
    # YOUR CODE HERE

screen = Screen()

frank = None    # YOUR CODE HERE
frank.left(180)
pete = None     # YOUR CODE HERE

# dont change anything below this comment

def move(t):
    t.move()
    screen.ontimer(lambda: move(t), 500)

move(frank)
move(pete)
screen.exitonclick()
