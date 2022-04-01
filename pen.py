from turtle import Turtle


class Pen(Turtle):

    def __init__(self, state, x, y):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.state = state
        self.x = x
        self.y = y

    def write_answer(self):
        self.goto(self.x, self.y)
        self.write(self.state)
