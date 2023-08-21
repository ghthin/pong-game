from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position_x, position_y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position_x, position_y)
        self.speed(0)

    def paddle_up(self):
        print(" up clicked")
        y = self.ycor()
        y += 20
        self.goto(self.xcor(), y)

    def paddle_down(self):
        y = self.ycor()
        y -= 20
        self.goto(self.xcor(), y)