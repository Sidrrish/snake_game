from turtle import Turtle
import random

STARTING_POSITIONS = [(0, 0), (0, 20), (0, 40)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
COLORS = ("beru",

          "dodgerblue",

          "lavender",

          "darkgoldenrod",

          "deepskyblue",

          "darkorchid",

          "ivory",

          "lightgoldenrodyellow",

          "teal",

          "brown",

          "lightgrey",

          "wheat",

          "turquoise",

          "khaki",

          "lightsalmon",

          "plum",

          "darkcyan",

          "Orange",

          "white",

          "palegoldenrod",

          "slategray",

          "darkmagenta",

          "bisque",

          "aquamarine",

          "springgreen",

          "dimgray",

          "chartreuse",

          "blanchedalmond",

          "papayawhip",

          "fuchsia",

          "mediumspringgreen",

          "seashell",

          "burlywood",

          "darkslategrey",

          "Palegreen", "Time",

          "navajowhite",

          "lightcoral",

          "tomato",

          "pink",

          "darkseagreen",

          "Olive",

          "darkolivegreen",

          "mistyrose",

          "red",

          "slategrey",

          "lightpink",



          "cornsilk",



          "powderblue",

          "purple",

          "coral",

          "cornflowerblue",

          "lightyellow",

          "darkturquoise",

          "honeydew",

          "cadetblue",

          "ghostwhite",

          "lemonchiffon",

          "lightblue",

          "lightgray",

          "olivedrab",

          "rosybrown",

          "gainsboro",

          "tan",

          "dimgrey",

          "magenta",

          "orchid",

          "lightgreen",



          "aliceblue")


class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for positions in STARTING_POSITIONS:
            self.add_segment(positions)

    def add_segment(self, positions):
        snake_parts = Turtle(shape="square")
        snake_parts.color(random.choice(COLORS))
        snake_parts.penup()
        snake_parts.goto(positions)
        self.snake_body.append(snake_parts)

    def extend(self):  # add a new segment
        self.add_segment(self.snake_body[-1].position())

    def move(self):
        for seg_num in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[seg_num - 1].xcor()
            new_y = self.snake_body[seg_num - 1].ycor()
            self.snake_body[seg_num].goto(new_x, new_y)
        self.snake_body[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)
