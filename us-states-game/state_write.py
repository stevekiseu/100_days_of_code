from turtle import Turtle
FONT = ("Arial", 11, "normal" )


class StateWrite(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()

    def fill_state(self, state, x, y):
        self.goto(x, y)
        self.write(state, align="center", font=FONT)





