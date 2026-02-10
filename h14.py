import turtle

turtle.speed(0)
pikk = 10
number = 1
screen = turtle.Screen()
pikkus = screen.numinput("Pikkuse sisestamine", "Mis on sinu pikkus?", default=20, minval=0, maxval=200)



for i in range(1, int(pikkus)):
    turtle.lt(90)
    turtle.fd(10+pikk)
    turtle.write(number, font=("Arial", 10, "normal"))
    turtle.bk(10+pikk)
    turtle.rt(90)
    turtle.fd(20)
    if i%5==0:
        pikk = 10
        turtle.write(i, font=("Arial", 10, "normal"))
    else:
        pikk = 0
    number += i


turtle.hideturtle
turtle.done()