from turtle import Turtle, Screen
import time
from snack_brain import Snack

screen = Screen()
screen.setup(width=600, height=600)
screen.title("My Snack Game")
screen.bgcolor("black")
screen.tracer(0)

snack_game = Snack()

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)

    snack_game.move()
    screen.listen()
    screen.onkey(snack_game.move_up , "Up")
    screen.onkey(snack_game.move_down, "Down")
    screen.onkey(snack_game.move_right, "Right")
    screen.onkey(snack_game.move_left, "Left")

screen.exitonclick()

