from turtle import Turtle
import random



class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.speed("fastest")
        self.penup()
        self.shapesize(1, 1)
        self.refresh()

    def refresh(self):
        x_cor = random.randint(-280, 280)       # 600 by 600 pixel      half is 300
        y_cor = random.randint(-280, 280)
        self.goto(x_cor, y_cor)
