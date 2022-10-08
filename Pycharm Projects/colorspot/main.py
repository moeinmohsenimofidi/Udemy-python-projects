import random
import turtle
from turtle import Turtle, Screen

all_turtle = []
is_race_on = False
colors = ["red", "blue", "orange", "yellow", "green", "purple"]
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput(title="Make your bet", prompt="which one will win the race?? select your color")
turtle.speed("fastest")
y_position = [-70, -40, -10, 20, 50, 80]
for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(-230, y_position[turtle_index])
    all_turtle.append(new_turtle)


if user_bet:
    is_race_on = True
while is_race_on:

    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            wining_color = turtle.pencolor()
            if wining_color == user_bet:
                print("you win")
            else:
                print(f"your lost, turtle {wining_color} won the game")
        random_step = random.randint(0, 10)
        turtle.forward(random_step)


screen.exitonclick()