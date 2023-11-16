import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=600, height=500)
user_bit = screen.textinput(title="make a bit", prompt="Which turtle will win the race and Enter the color")
colors = ["red", "yellow", "blue", "purple", "green", "orange"]
y_direction = [-70, -40, -10, 28, 58, 88]
ran = []

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_direction[turtle_index])
    ran.append(new_turtle)

if user_bit:
    is_race_on = True

while is_race_on:
    if turtle.xcor() > 230:
        is_race_on = False
        winning_color = turtle.pencolor()
        if winning_color == user_bit:
            print(f"you've won ! The {winning_color} turtle is winner")
        else:
            print(f"you've lost ! The {winning_color} turtle is winner")

    rand_dis = random.randint(0,10)
    turtle.forward(rand_dis)

screen.exitonclick()