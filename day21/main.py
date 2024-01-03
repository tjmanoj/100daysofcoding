from snake import Snake
from turtle import Screen
from food import Food
from scoreboard import Score
import time

screen = Screen()
screen.bgcolor("black")
screen.title("Snake Game!")
screen.screensize(600, 600)
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect food collision
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increment()
        snake.extend_snake()

    # detect wall collision

    if snake.head.ycor() > 320 or snake.head.ycor() < -320 or snake.head.xcor() > 380 or snake.head.xcor() < -380:
        is_game_on = False
        score.game_over()

    # detect self collision
    for segment in snake.snake_body[1:]:
        # if segment != snake.snake_body[0]:
            if snake.head.distance(segment) < 10:
                is_game_on = False
                score.game_over()

screen.exitonclick()
