from turtle import Turtle

MOVE_DISTANCE = 20

RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:
    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.snake_head = self.snake_segments[0]

    def create_snake(self):
        last_link_pos = (0, 0)
        for snake_link in range(3):
            new_snake_link = Turtle("square")
            new_snake_link.color("white")
            new_snake_link.up()

            self.snake_segments.append(new_snake_link)
            self.snake_segments[snake_link].goto(last_link_pos)
            self.snake_segments[snake_link].goto(
                self.snake_segments[snake_link].xcor() - 20,
                self.snake_segments[snake_link].ycor(),
            )
            last_link_pos = self.snake_segments[snake_link].pos()

    def move(self):
        for snake_link in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[snake_link - 1].xcor()
            new_y = self.snake_segments[snake_link - 1].ycor()

            self.snake_segments[snake_link].goto(new_x, new_y)
        self.snake_head.forward(MOVE_DISTANCE)

    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.seth(RIGHT)

    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.seth(UP)

    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.seth(LEFT)

    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.seth(DOWN)
