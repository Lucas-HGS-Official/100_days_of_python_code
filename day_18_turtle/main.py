from turtle import Screen, Turtle


def main():
    if __name__ == "__main__":
        turtle = Turtle()
        screen = Screen()

        turtle.color("red")

        for _ in range(10):
            turtle.forward(10)
            turtle.up()
            turtle.forward(10)
            turtle.down()

        screen.exitonclick()


main()
