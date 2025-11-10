import turtle
t = turtle.Turtle()
aken = turtle.Screen()
aken.title("Sinilill - Armin Cedric Allas")
# Kasutades värvide nimetusi
aken.setup(500,500)
t.pensize(10)
t.speed(0)

#vars
t.penup()
t.goto(0,-200)
t.pendown()
t.pencolor("green")
t.lt(90)
t.fd(200)
#õis
t.pencolor("blue")
t.rt(90)
t.circle(60)
t.begin_fill()
t.color("blue", "lightblue") # Must joon, punane täide
t.circle(60)
t.end_fill()
##emakas
t.penup()
t.goto(0,50)
t.pendown()
t.pencolor("yellow")
t.pensize(20)
t.circle(10)

#leht

t.penup()
t.goto(-20,-100)
t.pendown()
t.pencolor("green")
t.lt(90)
t.fd(40)
t.lt(135)
t.fd(35)
t.lt(100)
t.fd(30)
























turtle.done