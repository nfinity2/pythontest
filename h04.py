# Armin Cedric Allas
# 18.11.2025

#Ülesanne 03

# Loo muutuja sihtkoht, mis sisaldab reisi sihtkohta (string)
# Loo muutuja paevade_arv, mis näitab, mitu päeva reis kestab (integer)
# Loo muutuja oobimise_hind, mis näitab ühe öö hinna (float)
# Trüki välja lause, mis ühendab need andmed, nt: “Soome reis kestab 5 päeva ja üks öö maksab 30.50 eurot.”
# Kasuta väljatrükkimisel ainult komasid (,)

#3,3
sihtkoht = "Soome"
paevade_arv = "5"
oobimise_hind = "30.50"
print (sihtkoht, "reis kestab",paevade_arv, "paeva ja uks oo maksab", oobimise_hind, "eurot")

#3,1
nimi = "Armin"
vanus = "17"
keskmine_hinne = "3,5"
print (nimi, vanus, "aastat vana ja keskmine hinne on", keskmine_hinne)

#3,2
toode = "valge monsterit"
kogus = "22"
hind = "1,49"
print("Soovin "+kogus+" "+toode)

#3,4
raamatu_pealkiri = ("Karin Eegreid elulugu")
raamatu_autor = ("Imre Tard")
raamat = raamatu_pealkiri, raamatu_autor
lehekylgede_arv = ("539")
hindamisskoor = ("4/10")
print ("Minu lemmikraamat on", raamat,"mis on",lehekylgede_arv,"lehekülge pikk ja mille ma hindan",hindamisskoor)

#3,5
auto_mark = ("BMW")
auto_mudel = ("E46")
auto = auto_mark, auto_mudel
tootmistaasta = ("1998")
hind = ("5299€")
print("Minu unistuste auto on", auto, "aastast", tootmistaasta, "mille hind on", hind)

#3,6
import turtle

kylje_pikkus = 100
nurk = 90
kujundi_varv = "red" 
kogus = 3
nihe = 1.5
turtle.speed(0)
turtle.color(kujundi_varv)

for j in range(kogus):
    for i in range(4) :
        turtle.fd(kylje_pikkus)
        turtle.lt(nurk)
    turtle.penup()
    turtle.fd(kylje_pikkus*nihe)
    turtle.pendown()
    
turtle.done()

