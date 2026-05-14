import time
from turtle import Screen

from snake import Snake


def main():
    if __name__ == "__main__":
        screen = Screen()
        screen.setup(600, 600)
        screen.bgcolor("black")
        screen.title("Viper Game")
        screen.tracer(0)

        snake = Snake()

        screen.listen()
        screen.onkey(key="Up", fun=snake.up)
        screen.onkey(key="Down", fun=snake.down)
        screen.onkey(key="Left", fun=snake.left)
        screen.onkey(key="Right", fun=snake.right)

        screen.onkey(key="Escape", fun=screen.bye)

        is_game_start = True
        while is_game_start:
            snake.move()
            screen.update()
            time.sleep(0.1)

        screen.exitonclick()


main()
