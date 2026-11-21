from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()

        self.penup()
        self.shape("turtle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("yellow")
        self.speed(0)
        self.refresh()

    def refresh(self, occupied_positions=None):
        occupied_positions = occupied_positions or []

        while True:
            random_x = random.choice(range(-280, 281, 20))
            random_y = random.choice(range(-280, 281, 20))

            if (random_x, random_y) not in occupied_positions:
                self.goto(random_x, random_y)
                break
