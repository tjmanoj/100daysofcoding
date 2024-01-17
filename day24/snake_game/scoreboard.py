from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.score = 0
        self.increment()

    def increment(self):
        self.clear()
        self.setposition(0, 280)
        self.write(f"Score: {self.score}", align="center", font=('Arial', 18, 'normal'))
        self.score += 1

    def game_over(self):
        self.setposition(0, 0)
        self.write("GAME OVER!", align="center", font=('Arial', 18, 'normal'))

