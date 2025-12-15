# armin cedric allas
# ülesanne 09 | 15.12.2025

for i in range(1,21):
    print(i, end=" ")
print("\n--------------------------------------------------------")
loend = [60, 5, 4, 42, 99, 67, 47, 22, 34, 8, 85, 50, 94, 39, 54, 83, 27, 40, 17, 75]
paaris = []
paaritud = []


for i in loend:
    #print(i, end=" ")
    if i%2==0:
        paaris.append(i)
    else:
        paaritud.append(i)
print(f"paaris arvude summa on {sum(paaris)}")
print(f"paaritute arvude summa on {sum(paaritud)}")


for i in range(200,321):
    if i%7==0 and i%5!=0:
        print(i, end=", ")
        
parim_tyyp = ""
parim_keskmine = 0.0
h_tyyp =  ""
h_keskmine = 5.0
ryhma_hinded = ["Mari 4.9", "Jüri 3.1", "Kadri 4.6", "Marko 4.7", "Liis 4.9", "Andres 4.2", "Anu 4.7", "Martin 4.2", "Piret 4.2", "Tõnu 4.1"]
print(ryhma_hinded)
for i in (ryhma_hinded):
    nimi, keskmine = i.split(" ")
    if float(keskmine) > parim_keskmine:
        parim_tyyp = nimi
        parim_keskmine = float(keskmine)
    elif float(keskmine) < h_keskmine:
        h_tyyp = nimi
        h_keskmine = float(keskmine)

print(parim_tyyp)
print(h_tyyp)

    
#     print(nimi, keskmine)
    