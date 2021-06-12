from turtle import *

def compute_turn_angle(n):
    return 180 - (180 * (n - 2)) / n

def draw_ngon(n, sidelength = 100):
    for i in range(n):

        forward(sidelength)
        left(compute_turn_angle(n))

draw_ngon(7)
input()
