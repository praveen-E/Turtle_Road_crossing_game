from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()

    def create_player(self):
        self.penup()
        self.goto(STARTING_POSITION)
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.left(90)

    def move(self):
        self.fd(MOVE_DISTANCE)

    def next_level(self):
        if self.ycor() == FINISH_LINE_Y:
            return True

    def start_position(self):
        self.goto(STARTING_POSITION)
