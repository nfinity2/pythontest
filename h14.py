import turtle

turtle.speed(0)
pikk = 10
number = 0
screen = turtle.Screen()
pikkus = screen.numinput("Pikkuse sisestamine", "Mis on sinu pikkus?", default=20, minval=0, maxval=200)



for i in range(1, int(pikkus)):
    turtle.lt(90)
    turtle.fd(10+pikk)
    turtle.bk(10+pikk)
    turtle.rt(90)
    turtle.fd(20)
    if i%5==0:
        pikk = 10
    else:
        pikk = 0
    # number += i


turtle.goto(0,0)
turtle.lt(90)
turtle.fd(10+pikk+20)
turtle.rt(90)
turtle.penup()
for i in range(1, int(pikkus)):
    if number%5==0:
        turtle.write(number, font=("Arial", 8, "normal"))
    turtle.fd(20)
    number+=1

turtle.hideturtle
turtle.done()