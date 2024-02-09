import turtle
import pandas
import csv
screen = turtle.Screen()

writer = turtle.Turtle()

map_image = "blank_states_img.gif"
screen.addshape(map_image)

turtle.shape(map_image)
points = 0
data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
guessed_states = []
missed_state = []
def locate(name):
    answer = data[data["state"] == name]
    x_axis = int(answer.x)
    y_axis = int(answer.y)
    writer.hideturtle()
    writer.penup()
    writer.goto(x_axis, y_axis)
    writer.write(name)


def result():
    for i in states:
        if i not in guessed_states:
            missed_state.append(i)
    file = pandas.DataFrame(missed_state)
    file.to_csv("to_learn")


is_game_on = True


while is_game_on and len(guessed_states) < 50:
    state_name = screen.textinput(title=f"{points}/50 correct", prompt="Guess next state?").title()
    if state_name in states and state_name not in guessed_states:
        guessed_states.append(state_name)
        points += 1
        locate(state_name)
    elif state_name == "Exit":
        result()
        is_game_on = False
    else:
        continue








