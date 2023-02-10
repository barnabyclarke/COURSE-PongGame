from turtle import Turtle
MOVE_DISTANCE = 20


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.setheading(90)    # Rotate to face north
        self.color("white")
        self.shapesize(1, 5)    # Make it 'tall and skinny' (not 'fat and wide')
        self.goto(position)

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def move_down(self):
        self.back(MOVE_DISTANCE)
