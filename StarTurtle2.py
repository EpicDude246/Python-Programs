import turtle
import itertools
t = turtle.Turtle()
t.speed(0)
t.hideturtle()
col = ["Yellow", "Red", "Green", "Orange", "Purple", "Brown"]
list_cycle = itertools.cycle(col)
for i in range(50):
    c = next(list_cycle)
    t.pencolor(c)
    t.forward(i * 10)
    t.right(144)
