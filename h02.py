import turtle
t = turtle.Turtle()
aken = turtle.Screen()
aken.title("Olümpiarõngad - Armin Cedric Allas")
# Kasutades värvide nimetusi
t.pencolor("purple")
aken.setup(500,400)
#sinine
t.penup()
t.goto(-110,0)
t.pendown()
t.pensize(6)
t.pencolor("blue")
t.speed(0) # kiirus
t.circle(50) # ring
#must
t.penup()
t.goto(0,0)
t.pendown()
t.pensize(6)
t.pencolor("black")
t.speed(0) # kiirus
t.circle(50) # ring

t.penup()
t.goto(110,0)
t.pendown()
t.pensize(6)
t.pencolor("red")
t.speed(0) # kiirus
t.circle(50) # ring

t.penup()
t.goto(-60,-50)
t.pendown()
t.pensize(6)
t.pencolor("yellow")
t.speed(0) # kiirus
t.circle(50) # ring

t.penup()
t.goto(60,-50)
t.pendown()
t.pensize(6)
t.pencolor("green")
t.speed(0) # kiirus
t.circle(50) # ring










turtle.done()