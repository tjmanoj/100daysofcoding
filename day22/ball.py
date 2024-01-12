from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1

    def move(self):
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x, y)

    def move_y(self):
        self.y_move *= -1
        self.ball_speed *= 0.8

    def move_x(self):
        self.x_move *= -1
        self.ball_speed *= 0.8

    def reset_position(self):
        self.ball_speed = 0.1
        self.goto(0, 0)
        self.move_x()
