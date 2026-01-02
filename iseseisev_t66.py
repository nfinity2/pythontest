import turtle

turtle.speed(10)
turtle.pensize(2)

fw = 60
pikkus = fw * 0.5
laius = fw * 0.3

turtle.penup()
turtle.goto(-250, 0)
turtle.pendown()

for i in range(4):
    for i in range(2):
        turtle.forward(fw)
        turtle.left(90)
    
    turtle.forward(fw)
    turtle.right(90)

turtle.penup()
turtle.goto(150,0)
turtle.setheading(0)
turtle.pendown()

for i in range(8):
    turtle.forward(laius)
    
    for i in range(2):
        turtle.left(90)
        turtle.forward(fw)
        turtle.left(90)
        turtle.forward(laius)
    
    turtle.right(45)

turtle.hideturtle()
turtle.done()
