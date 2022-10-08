import turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()
turtle.colormode(255)
timmy.shape("turtle")

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

pensize = 10
direction = [0, 90, 180, 270]
extend = 1
timmy.speed("fastest")
#ef draw_shape(num_side):
#   for j in range(num_side):
#       timmy.forward(40)
#       timmy.right(360 / num_side)


#ef draw_shape1(num_side):
#   for j in range(num_side):
#       timmy.forward(40)
#       timmy.left(360 / num_side)


#or i in range(3, 20):
#   timmy.color(random.choice(colours))
#   draw_shape(i)
#   timmy.color(random.choice(colours))
#   draw_shape1(i)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color






for i in range(180):
    timmy.color(random_color())
    current_heading = timmy.heading()
    timmy.setheading(current_heading + 2)
    timmy.circle(100)




screen = Screen()
screen.exitonclick()

