import turtle
from turtle import Turtle, Screen
import random

my_turtle = Turtle()
turtle.colormode(255)

def draw_shap(new_sides):
    angle = 360 / new_sides
    for _ in range(new_sides):
        my_turtle.forward(100)
        my_turtle.right(angle)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

#color = ["silver", "dark gray", "red", "magenta", "dark violet"]
direction = [0, 90, 180, 270]
#my_turtle.pensize(15)
my_turtle.speed("fastest")

# my_turtle.shape("turtle")
# my_turtle.color("red")
# for sides in range(3 , 11):
#     my_turtle.color(random.choice(color))
#     draw_shap(sides)
def circle(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        my_turtle.color(random_color())
        my_turtle.circle(100)
        my_turtle.seth(my_turtle.heading() + 10)

circle(2)


my_screen = Screen()
my_screen.exitonclick()