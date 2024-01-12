from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.position = position
        self.create_paddle()
        self.position_of_paddle()

    def create_paddle(self):
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()

    def position_of_paddle(self):
        self.goto(self.position)

    def up(self):
        self.goto(self.xcor(), self.ycor() + 40)

    def down(self):
        self.goto(self.xcor(), self.ycor() - 40)

