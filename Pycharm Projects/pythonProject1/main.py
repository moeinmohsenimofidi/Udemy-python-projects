#from turtle import Turtle, Screen
#timmy = Turtle()
#timmy.shape("turtle")
#timmy.color("blue")
#timmy.forward(100)
#for i in range(100):
#    timmy.setx(i#)
#
#
#my_screen = Screen()
#print(my_screen.canvwidth)
#my_screen.exitonclick()
from prettytable import PrettyTable
table= PrettyTable()
table.add_column("pokemon name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("type", ["Electric", "Water", "Fire"])

table.align = "r"

print(table)