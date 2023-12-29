from turtle import Turtle, Screen
import time
from typing import Type

from snack_brain import Snack
from food import Food
from score_board import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("My Snack Game")
screen.bgcolor("black")
screen.tracer(0)

snack_game = Snack()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snack_game.move_up , "Up")
screen.onkey(snack_game.move_down, "Down")
screen.onkey(snack_game.move_right, "Right")
screen.onkey(snack_game.move_left, "Left")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)

    snack_game.move()
    if snack_game.head.distance(food) < 15:
        food.refresh()
        snack_game.extend()
        scoreboard.increase_score()

    if snack_game.head.xcor() > 280 or snack_game.head.xcor() < -280 or snack_game.head.ycor() < -280 or snack_game.head.ycor() > 280:
        is_game_on = False
        scoreboard.game_over()

    for segment in snack_game.segments[1:]:
        if snack_game.head.distance(segment) < 10:
            is_game_on = False
            scoreboard.game_over()

screen.exitonclick()

