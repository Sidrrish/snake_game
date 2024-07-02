from turtle import Turtle
import random
from snake import COLORS

TURTEL_SHAPES = ["turtle", "circle", "square"]

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape(random.choice(TURTEL_SHAPES))
        self.color("yellow")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.penup()
        self.speed("fastest")

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
