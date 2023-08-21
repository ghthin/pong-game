from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed(0)
        self.goto(0, 0)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        # new_x = self.xcor() + 10
        # new_y = self.ycor() + 10
        # self.goto(new_x, new_y)
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move

        # print(f"new_x: {new_x}, new_y: {new_y}")
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1
        # print(f"self.y_move: {self.y_move}")
        self.move_speed *= 0.9

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9
        # print(f"self.x_move: {self.x_move}")

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()


