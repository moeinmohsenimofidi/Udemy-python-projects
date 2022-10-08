from player import Screen
from player import Player

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Crossing Turtle")
screen.tracer(0.1)

player = Player()




screen.exitonclick()