import turtle

#Turtles
sun = turtle.Turtle()
ground = turtle.Turtle()
person = turtle.Turtle()

#Speed
sun.speed(0)
ground.speed(0)
person.speed(0)

#Hide turtles
sun.hideturtle()
ground.hideturtle()
person.hideturtle()

#Colors
turtle.bgcolor("deep sky blue")
sun.fillcolor("yellow")
ground.fillcolor("green")
person.fillcolor("blanched almond")

#Sun
sun.up()
sun.goto(-300, 200)
sun.down()
sun.begin_fill()
sun.circle(50)
sun.end_fill()

#Ground
ground.up()
ground.backward(5000)
ground.right(90)
ground.forward(150)
ground.left(90)
ground.begin_fill()
ground.down()
ground.forward(10000)
ground.right(90)
ground.forward(5000)
ground.right(90)
ground.forward(10000)
ground.right(90)
ground.forward(5000)
ground.end_fill()

#Person

    #Positioning
person.up()
person.left(90)
person.forward(50)
person.down()

    #Head
person.right(90)
person.begin_fill()
person.circle(50)
person.end_fill()

    #Shirt setup 1
person.pensize(20)
person.pencolor("dark orange")

    #Torso 1
person.right(90)
person.forward(30)

    #Arm setup
person.pensize(10)

    #Arm 1
person.right(35)
person.forward(85)
person.forward(5)
person.pencolor("blanched almond")
person.backward(5)
person.pencolor("dark orange")
person.backward(85)

    #Arm 2
person.left(70)
person.forward(85)
person.forward(5)
person.pencolor("blanched almond")
person.backward(5)
person.pencolor("dark orange")
person.backward(85)

    #Shirt setup 2
person.right(35)
person.pensize(20)
person.pencolor("dark orange")

    #Torso 2
person.forward(100)

    #Leg setup
person.pensize(10)
person.pencolor("dark slate blue")

    #Leg 1
person.right(30)
person.forward(115)
person.forward(5)
person.pencolor("slate gray")
person.backward(5)
person.pencolor("dark slate blue")
person.backward(115)

    #Leg 2
person.left(60)
person.forward(115)
person.forward(5)
person.pencolor("slate gray")
person.backward(5)
person.pencolor("dark slate blue")
person.backward(115)
