from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Roboto", 50, "normal"))
        self.goto(100, 200)
        self.write(self.l_score, align="center", font=("Roboto", 50, "normal"))

    def score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Roboto", 50, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Roboto", 50, "normal"))

