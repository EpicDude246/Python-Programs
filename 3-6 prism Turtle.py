import turtle
t = turtle.Turtle()
t.speed(100000)
y = 5
for x in range(25, 75):
    for y in range(3):
        t.forward(x)
        t.right(90)
    t.forward(x-y)
    t.right(90)
