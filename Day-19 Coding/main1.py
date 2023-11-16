from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def backward():
    tim.backward(10)
def counter_clock():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)
def clockwise():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)
def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=backward)
screen.onkey(key="a", fun=counter_clock)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()