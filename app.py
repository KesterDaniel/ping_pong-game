from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("ping-pong")
screen.tracer(0)

paddle_1 = Turtle()
paddle_1.penup()
paddle_1.color("white")
paddle_1.shape("square")
paddle_1.shapesize(stretch_wid=5, stretch_len=1)
paddle_1.goto(350, 0)


def up():
    paddle_1.sety(paddle_1.ycor() + 20)


def down():
    paddle_1.sety(paddle_1.ycor() - 20)


screen.listen()
screen.onkeypress(key="w", fun=up)
screen.onkeypress(key="s", fun=down)


game_is_on = True
while game_is_on:
    screen.update()


screen.exitonclick()
