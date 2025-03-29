from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 20, "bold")
COLOR = "white"


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        with open("score.txt") as file:
            self.highscore = int(file.read())
        self.pencolor(COLOR)
        self.penup()
        self.goto(x=0, y=260)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(
            arg=f"Score: {self.score} Highscore: {self.highscore} ",
            align=ALIGN,
            font=FONT,
        )

    def increase_score(self):
        self.score += 1
        self.update_score()

    def new_highscore(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("score.txt", mode="w") as file:
                file.write(f"{self.highscore}")

        self.score = 0
        self.update_score()
