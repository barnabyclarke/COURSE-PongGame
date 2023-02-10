from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.title("Welcome to Pong!")
screen.tracer(0)
screen.setup(width=800, height=600)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.03)
    screen.update()
    ball.move()

    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.wall_bounce()

    if ball.distance(l_paddle) <= 50 and ball.xcor() <= -330 or ball.distance(r_paddle) <= 50 and ball.xcor() >= 330:
        ball.paddle_bounce()

    if ball.xcor() > 380:    # Goal in RIGHT
        time.sleep(1)
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:    # Goal in LEFT
        time.sleep(1)
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
