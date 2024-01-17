from turtle import Turtle
FONT = ("Courier", 20, "normal")
POSITION = (-220, 250)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1

    def display(self):
        self.clear()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(POSITION)
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def game_over(self):
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(0, 0)
        self.write("Game Over!", align="center", font=FONT)

    def level_up(self):
        self.level += 1
