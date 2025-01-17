from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("White")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score} ", True, "Center", FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER ", True, "Center", FONT)

    def add_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()


