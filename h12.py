# Ülesanne 11

import turtle
import random

def pikim_sona(list):
    pikimarv = 0
    pikimNimi = " "
    for i in list:
        if len(i) > pikimarv:
            pikimarv = len(i)
            pikimNimi = i
    return pikimNimi


def kolm_pikimat_nime(list):
    if len(list)>2:
        list.sort(key=len, reverse=True)
        return list[0:3]
    else:
        return "tere"

def ruut(a):
    for i in range(4):
        turtle.forward(a)
        turtle.left(90)

nimed = ["Mari", "Mario","Anri", "Indrek"]


print(pikim_sona(nimed))
print(kolm_pikimat_nime(nimed))


for _ in range(57):
    turtle.speed(0)
    ruut(102)
    turtle.penup()
    turtle.goto(random.randint(700,200),(random.randint(0,300)))
    turtle.pendown()

turtle.done()