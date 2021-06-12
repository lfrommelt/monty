from random import randint, choice
from math import sin, cos, pi
from tkinter import *

def initialize(size):
    """Initializes a canvas of size x size pixels and returns it"""
    w = Tk()
    cv = Canvas(w, width=size, height=size, background="white")
    cv.pack()

    return cv

def draw_triangle(cv):
    """Draws am equilateral triangle on the given canvas.
    Returns the coordinates of the corners of the triangle as a list
    """
    size = int(cv["width"])
    r = size / 2

    triangle = [
        (cos(90/360 * 2 * pi) * r + size/2, -sin(90/360 * 2 * pi) * r + size/1.65),
        (cos(210/360 * 2 * pi) * r + size/2, -sin(210/360 * 2 * pi) * r + size/1.65),
        (cos(330/360 * 2 * pi) * r + size/2, -sin(330/360 * 2 * pi) * r + size/1.65)
    ]

    cv.create_line(triangle[0], triangle[1])
    cv.create_line(triangle[1], triangle[2])
    cv.create_line(triangle[2], triangle[0])

    return triangle

def random_point(cv):
    """Returns a random point on the canvas"""
    upper_bound = int(cv["width"]) - 1

    return (randint(0, upper_bound), randint(0, upper_bound))

def random_corner(triangle):
    """Returns a random vertex (corner) of the given triangle"""
    return choice(triangle)

def get_halfway_point(p1, p2):
    """Returns the coordinates of the point halfway between
    the two given points as a tuple
    """
    return (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2

def draw_point(p, cv):
    """Draws a given point onto the given canvas"""
    cv.create_line(p, (p[0] + 1, p[1] + 1), width=2)
    cv.update()
