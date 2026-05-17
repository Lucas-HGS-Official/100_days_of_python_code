import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.up()
        self.shapesize(stretch_len=0.3, stretch_wid=0.3)
        self.color("yellow")
        self.speed("fastest")
        self.set_rand_pos()

    def set_rand_pos(self):
        random_x = random.randint(-250, 250)
        random_y = random.randint(-250, 250)
        self.goto(random_x, random_y)
