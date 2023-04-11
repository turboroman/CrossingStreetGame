import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
scoreboard = Scoreboard()

screen.onkeypress(player.move, 'Up')


game_is_on = True
cars = CarManager()

count_for_new_car = 0
timer_speed = 0.1
while game_is_on:
    time.sleep(timer_speed)
    screen.update()
    cars.move()

    if count_for_new_car == 6:
        car = cars.generate_car()
        count_for_new_car = 0

    for car in cars.cars:
        if player.distance(car) < 25:
            game_is_on = False
            scoreboard.game_over()

    if player.finish():
        scoreboard.update_level()
        cars.increase_speed()
        timer_speed /= 2

    count_for_new_car += 1

screen.exitonclick()