from turtle import Screen
from turtle import Turtle

myScreen = Screen()
pong = Turtle("square")
myScreen.tracer(0)

myScreen.setup(800, 600)
myScreen.bgcolor("black")
myScreen.title("Pong")

pong.color("white")
pong.shapesize(8, 1.5)
pong.penup()
pong.goto(250, 0)
myScreen.tracer(1)
myScreen.exitonclick()
