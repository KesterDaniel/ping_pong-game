from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, xpos, ypos):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(xpos, ypos)
        self.write(self.score, align="center", font=('Elephant', 35, 'normal'))

    def update(self):
        self.clear()
        self.score += 1
        self.write(self.score, align="center", font=('Elephant', 35, 'normal'))
