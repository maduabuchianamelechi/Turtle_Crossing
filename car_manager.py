from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    
    def __init__(self):
        self.cars = []

    def create_car(self):
        rand_num = random.randint(1, 6)
        if rand_num == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            rand_y = random.randint(-250, 250)
            new_car.goto(300, rand_y)
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.backward(STARTING_MOVE_DISTANCE)
