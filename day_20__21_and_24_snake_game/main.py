import time
from turtle import Screen

from food import Food
from scoreboard import ScoreBoard
from snake import Snake

is_game_start = True


def main():
    if __name__ == "__main__":
        screen = Screen()
        screen.setup(600, 600)
        screen.bgcolor("black")
        screen.title("Viper Game")
        screen.tracer(0)

        global snake
        snake = Snake()
        food = Food()

        global scoreboard
        scoreboard = ScoreBoard()

        screen.listen()
        screen.onkey(key="Up", fun=snake.up)
        screen.onkey(key="Down", fun=snake.down)
        screen.onkey(key="Left", fun=snake.left)
        screen.onkey(key="Right", fun=snake.right)

        screen.onkey(key="Escape", fun=screen.bye)

        global is_game_start
        is_game_start = is_game_start

        while is_game_start:
            print(is_game_start)
            snake.move()
            screen.update()
            time.sleep(0.15)

            if snake.snake_head.distance(food) < 15:
                food.set_rand_pos()
                scoreboard.increase_score()
                snake.add_segment()

            if (
                -280 > snake.snake_head.xcor()
                or snake.snake_head.xcor() > 280
                or -280 > snake.snake_head.ycor()
                or snake.snake_head.ycor() > 280
            ):
                is_game_start = False
                scoreboard.game_over()

            for segment in snake.snake_segments[1:]:
                if snake.snake_head.distance(segment) < 10:
                    is_game_start = False
                    scoreboard.game_over()

            if not is_game_start:
                screen.onkeypress(key="Return", fun=reset_game)

        screen.exitonclick()


def reset_game():
    scoreboard.reset_score()
    snake.reset_snake()
    global is_game_start
    is_game_start = True


main()
