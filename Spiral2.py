import turtle
import itertools
t=turtle.Pen()
c = ""
num = 1
col = ["Yellow", "Red", "Green", "Orange", "Purple", "Brown"]
list_cycle = itertools.cycle(col)
for x in range(50,1000,10):
    c = next(list_cycle)
    t.pencolor(c)
    t.forward(x)
    t.right(90)
    num = num+1
    if num == 4:
        num = 1
