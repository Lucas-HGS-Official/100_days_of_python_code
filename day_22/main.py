import random
import time
from turtle import Screen

from ball import Ball
from paddle import Paddle

WINDOW_HEIGHT = 600
WINDOW_WIDTH = 800
CURRENT_COLOR_MODE = 255
BG_COLOR = (29, 57, 44)

PADDLE_1_INIT_POS = (-WINDOW_WIDTH / 2 + 30, 0)
PADDLE_2_INIT_POS = (+WINDOW_WIDTH / 2 - (30 + (9 * 0.7)), 0)

screen = Screen()

is_game_start = True


def main():
    if __name__ == "__main__":
        screen.setup(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
        screen.colormode(CURRENT_COLOR_MODE)
        screen.bgcolor(BG_COLOR)
        screen.title("Pong Game")
        screen.tracer(0)
        screen.mode("logo")

        paddle_1 = Paddle(PADDLE_1_INIT_POS)
        paddle_2 = Paddle(PADDLE_2_INIT_POS)

        ball = Ball()

        screen.listen()

        screen.onkeypress(key="w", fun=paddle_1.move_up)
        screen.onkeypress(key="s", fun=paddle_1.move_down)

        screen.onkeypress(key="Up", fun=paddle_2.move_up)
        screen.onkeypress(key="Down", fun=paddle_2.move_down)

        screen.onkey(key="Escape", fun=close_game)

        global is_game_start
        while is_game_start:
            ball.update()
            screen.update()

            if ball.distance((paddle_1.pos())) == 10:
                # screen.mode("logo")
                ball.seth(random.randint(0, 180))
                print("test")
            elif ball.distance(paddle_2.pos()) == 10:
                # screen.mode("standard")
                ball.seth(random.randint(90, 270))
                print("test")

        if not is_game_start:
            screen.bye()


def close_game():
    global is_game_start
    is_game_start = False


main()
