from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("ping-pong")
screen.tracer(0)


def game():
    l_paddle = Paddle(-350)
    r_paddle = Paddle(350)
    ball = Ball()

    screen.listen()
    screen.onkeypress(key="w", fun=l_paddle.up)
    screen.onkeypress(key="s", fun=l_paddle.down)
    screen.onkeypress(key="o", fun=r_paddle.up)
    screen.onkeypress(key="l", fun=r_paddle.down)

    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
        screen.update()
        ball.move()
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()

        if ball.xcor() > 320 and ball.distance(r_paddle) < 50 or ball.xcor() < - 320 and ball.distance(l_paddle) < 50:
            ball.bounce_x()

        if ball.xcor() > 380:
            time.sleep(0.2)
            ball.reset_position()

        if ball.xcor() < -380:
            time.sleep(0.2)
            ball.reset_position()


game()
screen.exitonclick()
