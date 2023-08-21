import time
from turtle import Screen, Turtle

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
# set the screen size to 800 x 600
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(r_paddle.paddle_up, "Up")
screen.onkey(r_paddle.paddle_down, "Down")
screen.onkey(l_paddle.paddle_up, "w")
screen.onkey(l_paddle.paddle_down, "s")

game_is_0n = True
while game_is_0n:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # needs to bounce
        ball.bounce_y()  # call the bounce_y method from ball.py
    # detect collision with r_paddle and l_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()  # call the bounce_x method from ball.py

    # detect when l_paddle misses
    if ball.xcor() < -380:
        # print("l_paddle misses")
        ball.reset_position()
        # ball.bounce_x()
        scoreboard.r_point()

    # detect when r_paddle misses
    if ball.xcor() > 380:
        # print("r_paddle misses")
        ball.reset_position()
        # ball.bounce_x()
        scoreboard.l_point()

screen.exitonclick()
