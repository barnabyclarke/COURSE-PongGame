from turtle import Turtle
import random
BALL_SPEED = 6


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.modifier = [0, 90, 180, 270]
        self.ball_speed = BALL_SPEED
        self.shape("circle")
        self.color("white")
        self.penup()
        self.direction = random.randint(30, 60) + random.choice(self.modifier)
        self.setheading(self.direction)

    def randomizer(self):
        new_heading = random.randint(30, 60) + random.choice(self.modifier)
        self.direction = new_heading
        self.setheading(self.direction)

    def move(self):
        self.forward(self.ball_speed)

    def wall_bounce(self):
        new_heading = (360 - self.direction)
        self.direction = new_heading
        self.setheading(new_heading)

    def paddle_bounce(self):
        new_heading = (540 - self.direction + random.randint(-10, 10))
        self.direction = new_heading
        self.setheading(new_heading)
        self.ball_speed += 2

    def reset_position(self):
        self.goto(0, 0)
        self.ball_speed = BALL_SPEED
        self.randomizer()
