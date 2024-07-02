import turtle
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.up, "w")

screen.onkey(snake.down, "Down")
screen.onkey(snake.down, "s")

screen.onkey(snake.left, "Left")
screen.onkey(snake.left, "a")

screen.onkey(snake.right, "Right")
screen.onkey(snake.right, "d")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect food collision
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.goto(0, 270)
        scoreboard.add_score()

    # Detect collision with Wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.game_over()
        game_is_on = False

    # Detect collison with tail
    for snake_parts in snake.snake_body[1::]:

        if snake.head.distance(snake_parts) < 10:
            game_is_on = False
            scoreboard.game_over()




screen.exitonclick()
