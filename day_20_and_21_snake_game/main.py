import time
from turtle import Screen

from food import Food
from scoreboard import ScoreBoard
from snake import Snake


def main():
    if __name__ == "__main__":
        screen = Screen()
        screen.setup(600, 600)
        screen.bgcolor("black")
        screen.title("Viper Game")
        screen.tracer(0)

        snake = Snake()
        food = Food()

        scoreboard = ScoreBoard()

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

        screen.exitonclick()


main()
