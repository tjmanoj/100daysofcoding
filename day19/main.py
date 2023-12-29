import random
from turtle import Turtle
from turtle import Screen
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
screen = Screen()
screen.setup(width=500, height=400)
choice = screen.textinput(title="Turtle Game",
                          prompt="Which turtle will win the race, choose a color?")

y = -130
for color in colors:
    bubu = Turtle(shape="turtle")
    bubu.color(color)
    bubu.penup()
    bubu.goto(x=-230, y=y)
    y += 50
    all_turtles.append(bubu)

is_game_over = False
while not is_game_over:
    for turtle in all_turtles:
        if turtle.xcor() > 230 and choice == turtle.pencolor():
            print("You're turtle wins")
            is_game_over = True
        elif turtle.xcor() > 230:
            print(f"You lost! The {turtle.pencolor()} turtle wins")
            is_game_over = True

        random_speed = random.randint(0, 10)
        turtle.forward(random_speed)
screen.exitonclick()