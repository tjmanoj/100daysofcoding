import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
level = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_cars()
    car.move()
    level.display()

    # detect collision with cars
    for curr_car in car.all_cars:
        if player.distance(curr_car) < 25:
            level.game_over()
            game_is_on = False

    # detect collision with wall
    if player.ycor() > 280:
        player.restart()
        level.level_up()
        car.speed_up()


screen.exitonclick()
