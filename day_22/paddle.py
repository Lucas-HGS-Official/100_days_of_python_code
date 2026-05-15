from turtle import Turtle

PADDLE_COLOR = (216, 216, 216)
PADDLE_STRETCH_WIDTH = 3
PADDLE_STRETCH_HEIGHT = 0.7


class Paddle(Turtle):
    def __init__(self, initial_pos) -> None:
        super().__init__("square")
        self.initial_pos = initial_pos
        self.color(PADDLE_COLOR)
        self.up()
        self.shapesize(PADDLE_STRETCH_HEIGHT, PADDLE_STRETCH_WIDTH)
        self.seth(0)
        self.speed(0)
        self.goto(self.initial_pos)

    def move_up(self):
        self.forward(10)

    def move_down(self):
        self.backward(10)
