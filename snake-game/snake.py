from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.start = 0
        self.all_snakes = []
        self.create_snake()
        self.head = self.all_snakes[0]

    def create_snake(self):
        for i in range(3):
            self.add_turtle()

    def add_turtle(self):
        new_turtle = Turtle()
        new_turtle.color("white")
        new_turtle.shape("square")
        new_turtle.penup()
        new_turtle.goto(self.start, 0)
        self.all_snakes.append(new_turtle)
        self.start -= 20

    def extend(self):
        self.add_turtle()

    def move(self):
        for position in range(len(self.all_snakes) - 1, 0, -1):
            new_x = self.all_snakes[position - 1].xcor()
            new_y = self.all_snakes[position - 1].ycor()
            self.all_snakes[position].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
