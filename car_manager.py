from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        super().__init__()
        self.random_cars = []

    def create_car(self):
        car = Turtle()
        car.penup()
        car.shape("square")
        car.shapesize(1, 2)
        car.color(random.choice(COLORS))
        new_y = random.randint(-250, 250)
        car.goto(x=300, y=new_y)
        car.setheading(180)
        self.random_cars.append(car)

    def car_move(self, inc):
        for i in self.random_cars:
            i.fd(STARTING_MOVE_DISTANCE + inc*MOVE_INCREMENT)
