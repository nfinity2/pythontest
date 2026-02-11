import turtle
turtle.speed(0)
ekraan = turtle.Screen()
# pikkus = ekraan.numinput("Vali kujund", "1: Ruut \n2: Ring", default=20, minval=0, maxval=200)


def punane():
    turtle.color("Red")
def rohleine():
    turtle.color("Green")
def sinine():
    turtle.color("Blue")

ekraan.onkey(punane, "r")
ekraan.onkey(rohleine, "g")
ekraan.onkey(sinine, "b")


def vasakKlikk(x, y,):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    
    for _ in range (4):
        turtle.fd(100)
        turtle.lt(90)

def paremKlikk(x, y):
    for _ in range(8):
         turtle.undo()


ekraan.onscreenclick(vasakKlikk, 1) # Vasak klõps
ekraan.onscreenclick(paremKlikk, 3) # Parem klõps


ekraan.listen()
turtle.mainloop()