import turtle
import pandas
screen = turtle.Screen()

writer = turtle.Turtle()

map_image = "blank_states_img.gif"
screen.addshape(map_image)

turtle.shape(map_image)
points = 0
data = pandas.read_csv("50_states.csv")


def locate(name):
    answer = data[data["state"] == name]
    x_axis = int(answer.x)
    y_axis = int(answer.y)
    writer.hideturtle()
    writer.penup()
    writer.goto(x_axis, y_axis)

    writer.write(name)


state_name = screen.textinput(title=f"{points}/50 correct", prompt="Guess next state?")
locate(state_name)
screen.mainloop()








