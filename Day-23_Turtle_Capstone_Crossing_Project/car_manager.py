import turtle
from turtle import Turtle
from random import choice, randint

turtle.register_shape('green-car.gif')
turtle.register_shape('red-car.gif')
turtle.register_shape('police-car.gif')
turtle.register_shape('jeep.gif')
turtle.register_shape('pickup.gif')
turtle.register_shape('truck.gif')

car_list = ['green-car', 'red-car', 'police-car', 'jeep', 'pickup', 'truck']

SPAWN_POSITION_Y_AXIS = [-250, -200, -150, -100, -50, 0, 50, 100, 150, 200, 250]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = randint(1, 6)
        if random_chance == 1:
            new_car = Turtle(choice(car_list) + ".gif")
            new_car.penup()
            new_car.goto(x=300, y=choice(SPAWN_POSITION_Y_AXIS))
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
