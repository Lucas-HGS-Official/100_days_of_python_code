import random
from turtle import Screen, Turtle


def turtle_race(turtles_list):
    for turtle in turtles_list:
        if turtle.xcor() >= 230:
            return turtle.pencolor()
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


def main():
    if __name__ == "__main__":
        color_list = ["red", "orange", "yellow", "green", "blue", "purple"]
        turtles_list = []
        for _ in range(6):
            new_turtle = Turtle(shape="turtle")
            new_turtle.color(color_list[_])
            turtles_list.append(new_turtle)

        screen = Screen()
        screen.setup(width=500, height=400)
        race_start = False

        user_bet = screen.textinput(
            title="Make Your Bet!!",
            prompt=f"Which turtle will win? Enter a color: {color_list}",
        )

        turtles_initial_y = -100

        for turtle in range(len(turtles_list)):
            turtles_list[turtle].up()
            turtles_list[turtle].goto(x=-235, y=turtles_initial_y)
            turtles_initial_y += 40

        if user_bet:
            race_start = True

        print(user_bet)

        if race_start:
            while race_start:
                winner_color = turtle_race(turtles_list)
                if winner_color in color_list:
                    race_start = False
                    if winner_color == user_bet or user_bet == "win":
                        print(f"You've won! The {winner_color} turtle is the winner!")
                    else:
                        print(
                            f"You've lost... The {winner_color} turtle is the winner!"
                        )
                    print(winner_color)

        screen.exitonclick()


main()
