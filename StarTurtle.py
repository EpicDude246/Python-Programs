import turtle
t = turtle.Turtle()
t.speed(0)
t.hideturtle()
points = int(input("Points? "))
for x in range(points):
    t.right(15)
    t.forward(100)
    t.right(15)
    t.backward(100)
