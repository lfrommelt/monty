from turtle import *

setup(320, 320)

def draw_spiral(loops):
    for i in range(4 * loops):
        forward(10 * i)
        left(90)

draw_spiral(5)

getscreen().getcanvas().postscript(file = "spiral4.eps")

input()
