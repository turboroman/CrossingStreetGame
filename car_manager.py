from turtle import Turtle
from random import randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        # super().__init__()
        self.cars = []
        self.cars_speed = STARTING_MOVE_DISTANCE

    def generate_car(self):
        car = Turtle()
        car.shape('square')
        car.shapesize(1, 2)
        car.color(COLORS[randint(0, len(COLORS)-1)])
        car.penup()
        car.speed = self.cars_speed
        car.goto(300, randint(-250, 250))
        self.cars.append(car)
        return car

    def move(self):
        for car in self.cars:
            car.backward(car.speed)

    def increase_speed(self):
        self.cars_speed += MOVE_INCREMENT
