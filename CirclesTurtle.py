import turtle
t = turtle.Turtle()
t.speed(0)
t.up()
t.goto(0, 240)
t.down()
def circle(t):
    for x in range(74):
        t.forward(2)
        t.right(5)
circle(t)
for x in range(50):
    t.up()
    t.forward(100)
    t.down()
    circle(t)
#or
#t.speed(0)
#t.circle(100)
