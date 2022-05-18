from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput("make your bet", "Which turtle will win the race? Enter the color")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
start = -60
all_turtles = []

for color in colors:
    new_turtle = Turtle("turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(-230, start)
    start += 30
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        turtle.forward(random.randint(0, 10))
        if turtle.xcor() > 220:
            winner_color = turtle.fillcolor()
            is_race_on = False
            if winner_color == user_bet:
                print("You won the bet")
            else:
                print("You lost the bet")



screen.exitonclick()