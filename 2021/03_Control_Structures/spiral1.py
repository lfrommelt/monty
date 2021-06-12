from turtle import *

setup(600, 320)

up()
backward(150)
down()

for i in range(20):
    forward(10 * i)
    left(90)

up()
forward(400)
left(90)
forward(100)
right(90)
down()

for i in range(20):
    forward(10 * i)
    left(90)

getscreen().getcanvas().postscript(file = "spiral2.eps")

input()
