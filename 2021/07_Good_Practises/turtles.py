from turtle import Screen, Turtle

screen = Screen()

t1 = Turtle()

screen.ontimer(lambda: t1.forward(100), 100)
