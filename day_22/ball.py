import random
from turtle import Turtle

BALL_STRETCH = 0.5
BALL_COLOR = (216, 216, 216)


class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__("circle")
        self.color(BALL_COLOR)
        self.up()
        self.shapesize(BALL_STRETCH)
        self.speed(0)
        self.seth(90)
        # self.seth(random.randint(0, 180))

    def update(self):
        self.forward(0.1)
