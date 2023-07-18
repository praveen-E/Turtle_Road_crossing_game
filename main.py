import time
from turtle import Screen,Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
screen.listen()
screen.onkey(key="Up", fun=player.move)
cars = CarManager()
count = 0
level = 0
score = Scoreboard()
game_is_on = True
player.create_player()
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if count % (6-(level+1)) == 0:
        cars.create_car()

    for car in cars.random_cars:
        if player.distance(car) < 20:
            score.game_over()
            game_is_on = False

    if player.next_level():
        level += 1
        player.start_position()
        score.update_score(level)

    cars.car_move(level)
    count += 1

screen.exitonclick()
