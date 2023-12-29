from turtle import Turtle
STARTING_POSTION = [(0,0), (-20,0),(-40,0)]
MOVE_DISTANCE = 2
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snack:

    def __init__(self):
        self.segments = []
        self.creat_snack()
        self.head = self.segments[0]

    def creat_snack(self):
        for postion in STARTING_POSTION:
            self.add_segment(postion)

    def add_segment(self, postion):
        snack = Turtle("square")
        snack.color("white")
        snack.penup()
        snack.goto(postion)
        self.segments.append(snack)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.segments[0].forward(20)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)