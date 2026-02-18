import turtle
import random


skoor = 0

aken = turtle.Screen()
aken.bgcolor("lightblue")
aken.setup(width=600, height=600)
aken.tracer(0)

# ristkülik
ristkylik = turtle.Turtle()
ristkylik.shape("square")
ristkylik.shapesize(stretch_wid=1, stretch_len=5)
ristkylik.penup()
ristkylik.color("black")
ristkylik.goto(ristkylik.xcor(), -250)

# ring
ring = turtle.Turtle()
ring.shape("circle")
ring.penup()
ring.speed('fastest')
ring.setheading(random.randint(0, 360))

# kiirused
ristkyliku_kiirus = 20
kiirus = 10

# ristküliku funktsioonid
def liigu_vasakule():
    x = ristkylik.xcor()
    y = ristkylik.ycor()
    if x > -280:
        ristkylik.setx(x - ristkyliku_kiirus)

def liigu_paremale():
    x = ristkylik.xcor()
    if x < 280:
        ristkylik.setx(x + ristkyliku_kiirus)

# ringi funktsioonid
def peegelda_porkumisel():
    global skoor
    nurk = ring.heading()
    if ring.xcor() >= 300 or ring.xcor() <= -300:
        uus_nurk = 180 - nurk
        if uus_nurk < 0:
            uus_nurk += 360
        ring.setheading(uus_nurk)
    if ring.ycor() >= 300 or ring.ycor() <= -300:
        uus_nurk = 360 - nurk
        ring.setheading(uus_nurk)
    if (ring.ycor())<=-300:
        print("Game Over!")
    x = ristkylik.xcor()
    y = ristkylik.ycor()
    if (ring.ycor() <= y and ring.ycor()+5 >= y) and (ring.xcor() <= x and ring.xcor()+100 >= x):
        skoor+=1
        turtle.hideturtle()
        turtle.clear()
        turtle.penup()
        turtle.goto(-250,250)
        turtle.pendown
        turtle.write(skoor, font=("Arial", 30, "normal"))
        print("Skoor:",skoor)
        uus_nurk = 360 - nurk
        ring.setheading(uus_nurk)


def ring_liigu():
    ring.forward(kiirus)
    peegelda_porkumisel()
    aken.update()
    aken.ontimer(ring_liigu, 20)



# klaviatuurile reageerimine
aken.listen()
aken.onkeypress(liigu_vasakule, "Left")
aken.onkeypress(liigu_paremale, "Right")

ring_liigu()

aken.mainloop()