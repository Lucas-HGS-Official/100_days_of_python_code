from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 15, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0  # TODO: read highscore from file
        with open("highscore.txt", mode="r") as highscore_file:
            self.highscore = int(highscore_file.read())
        self.color("white")
        self.hideturtle()
        self.up()
        self.speed("fastest")
        self.goto(x=0, y=250)

        self.write_score()

    def write_score(self):
        self.write(
            arg=f"Score: {self.score} Highscore: {self.highscore}",
            align=ALIGN,
            font=FONT,
        )

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write_score()

    def game_over(self):
        self.goto(0, 0)
        if self.score > self.highscore:
            self.highscore = self.score
        self.write(arg="GAME OVER!", align=ALIGN, font=FONT)
        with open("highscore.txt", mode="w") as highscore_file:
            highscore_file.write(f"{self.highscore}")

    def reset_score(self):
        self.score = 0
        self.clear()
        self.goto(x=0, y=250)
        self.write_score()
