from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.shapesize(0.5)
        self.color('blue')
        self.penup()
        self.random_food()

    def random_food(self):
        self.goto(random.randint(-280, 280),random.randint(-280, 280))


            