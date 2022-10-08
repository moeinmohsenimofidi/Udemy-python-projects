import time
from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 3
        self.y_move = 3
        self.move_speed = 0.1

    def ball_move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def y_bounce(self):
        self.y_move *= -1


    def x_bounce(self):
        self.x_move *= -1
        self.move_speed *= 0.2

    def reset_position(self):
        self.goto(0, 0)
        time.sleep(0.3)
        self.move_speed = 0.1
        self.x_bounce()

