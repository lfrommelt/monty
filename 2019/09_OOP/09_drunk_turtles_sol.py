from turtle import Screen, Turtle
from random import random

class DrunkTurtle(Turtle):
    """A turtle that can move in a zig-zaggy way while singing a song"""
    def __init__(self, step_size, angle_limit, song):
        """Create a new DrunkTurtle with given parameters."""
        super().__init__()

        self._song = song
        self._step_size = step_size
        self._angle_limit = angle_limit
        self._step = 0

    def sing(self):
        """Sing the current word in the song based on self._step.
        Does not (!) increment self._step.
        """
        self.write(self._song[self._step % len(self._song)])

    def move(self):
        """Turns the turtle by a random angle, then moves it forward by self._step_size.
        Calls self.sing() to sing the next word of the song and handles self._step
        """
        self.left((2 * random() - 1) * self._angle_limit)
        self.forward(self._step_size)

        self.sing()

        self._step += 1

screen = Screen()

# instanciate two DrunkTurtles
frank = DrunkTurtle(step_size=20, angle_limit=20, song=["oh", "la", "la", "la."])
frank.left(180)
pete = DrunkTurtle(step_size=40, angle_limit=45, song=["shoo", "wa", "da", "dub."])

# dont change anything below this comment

def move(t):
    t.move()
    screen.ontimer(lambda: move(t), 500)

move(frank)
move(pete)
screen.exitonclick()
