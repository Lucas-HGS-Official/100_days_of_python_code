from turtle import Screen, Turtle

tim = Turtle()


def move_fowards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def move_clockwise():
    tim.setheading(tim.heading() + 10)


def move_counter_clockwise():
    tim.setheading(tim.heading() - 10)


def move_clear():
    tim.clear()
    tim.up()
    tim.home()
    tim.down()


def main():
    if __name__ == "__main__":
        screen = Screen()

        screen.listen()
        screen.onkeypress(key="w", fun=move_fowards)
        screen.onkeypress(key="s", fun=move_backwards)
        screen.onkeypress(key="d", fun=move_clockwise)
        screen.onkeypress(key="a", fun=move_counter_clockwise)

        screen.onkeypress(key="c", fun=move_clear)

        screen.exitonclick()


main()
