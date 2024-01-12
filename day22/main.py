import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score

myScreen = Screen()
myScreen.tracer(0)
myScreen.setup(800, 600)
myScreen.bgcolor("black")
myScreen.title("Pong")

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Score()

myScreen.listen()
myScreen.onkey(r_paddle.up, "Up")
myScreen.onkey(r_paddle.down, "Down")

myScreen.onkey(l_paddle.up, "w")
myScreen.onkey(l_paddle.down, "s")

is_game_on = True
while is_game_on:
    time.sleep(ball.ball_speed)
    myScreen.update()
    ball.move()

    # detecting collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.move_y()

    # collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.move_x()

    # right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_score += 1
        score.score()

    # left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_score += 1
        score.score()

myScreen.exitonclick()
