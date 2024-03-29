from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.starting_move_distance = 5

    def create_cars(self):
        flag = random.randint(1, 5)
        if flag == 1:
            car = Turtle("square")
            car.shapesize(stretch_len=2)
            car.penup()
            car.color(random.choice(COLORS))
            y_range = random.randint(-250, 240)
            car.goto(280, y_range)
            self.all_cars.append(car)

    def move(self):
        for car in self.all_cars:
            car.backward(self.starting_move_distance)

    def speed_up(self):
        self.starting_move_distance += MOVE_INCREMENT
