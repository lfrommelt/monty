from turtle import *


def plot_parabola():

    for x in range(-5, 6):
        goto(x * 60, x ** 2 * 60)

plot_parabola()
input()
