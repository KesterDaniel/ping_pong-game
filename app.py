from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("ping-pong")
screen.tracer(0)


l_paddle = Paddle(-350)
r_paddle = Paddle(350)
r_score_board = Scoreboard(50, 250)
l_score_board = Scoreboard(-50, 250)

ball = Ball()

screen.listen()
screen.onkeypress(key="w", fun=l_paddle.up)
screen.onkeypress(key="s", fun=l_paddle.down)
screen.onkeypress(key="o", fun=r_paddle.up)
screen.onkeypress(key="l", fun=r_paddle.down)

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect ball collision with y axis
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect ball collision with paddle
    if ball.xcor() > 320 and ball.distance(r_paddle) < 50 or ball.xcor() < - 320 and ball.distance(l_paddle) < 50:
        ball.bounce_x()

    # detect if ball has eluded right paddle
    if ball.xcor() > 380:
        time.sleep(0.2)
        l_score_board.update()
        ball.reset_position()

    # detect if ball has eluded left paddle
    if ball.xcor() < -380:
        time.sleep(0.2)
        r_score_board.update()
        ball.reset_position()


screen.exitonclick()
