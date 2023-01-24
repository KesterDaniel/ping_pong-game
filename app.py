from turtle import Screen, Turtle
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("ping-pong")
screen.tracer(0)

l_paddle = Paddle(-350)
r_paddle = Paddle(350)


screen.listen()
screen.onkeypress(key="w", fun=l_paddle.up)
screen.onkeypress(key="s", fun=l_paddle.down)
screen.onkeypress(key="o", fun=r_paddle.up)
screen.onkeypress(key="l", fun=r_paddle.down)


game_is_on = True
while game_is_on:
    screen.update()


screen.exitonclick()
