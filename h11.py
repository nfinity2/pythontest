# Koosta programm, mis genereerib ja kuvab korrutustabeli, kus iga number korrutatakse iseendaga


#9.8

for i in range(11):
    print(f"{i} * {i} = {i*i}")
    
#9.9
# Loo programm, mis loob suvalised tehted 1-100 arvudega.

import random
tehe = ["+", "-", "*", "/"]

punktid = 0
kysimuste_arv = 5
for _ in range(kysimuste_arv):
    arv1 = random.randint(1,10)
    arv2 = random.randint(1,10)
    t = random.choice(tehe)
    
    if t=="+":
        print(f"{arv1} {t} {arv2}=")
        v = int(input("vastus: "))
        if arv1+arv2 == v:
            punktid+1
            
    elif t=="-":
        print(f"{arv1} {t} {arv2}=")
        v = int(input("vastus: "))
        if arv1-arv2 == v:
            punktid+1
        
    elif t=="*":
        print(f"{arv1} {t} {arv2}=")
        v = int(input("vastus: "))
        if arv1*arv2 == v:
            punktid+1
            
    else:
        print(f"{arv1} {t} {arv2}=")
        v = float(input("vastus: "))
        if round (arv1/arv2,1) == v:
            punktid+1


if punktid/kysimuste_arv >= 0.5:
    print("A")
else:
    print("MA")
print(punktid)

#9.11 Kuva samasugused kujundid:



#1
arv = 5
for i in range (1,6):
    print(" " * i + "*" * arv)
    arv-=1

#2
arv = 5
for i in range (1,6):
    print("*" * arv)
    arv-=1


# #3
arv = 5
for i in range (1,6):
    print(" " * arv + "*" * i)
    arv-=1

#4
for i in range (1,6):
    print("*" * i)

# 9.12

summa = 0
even_nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 3, 32, 34, 36, 38]
for i in even_nums:
    if i%2==0:
        summa+=i
    else:
        break


print(summa)


print(" ")
# 9.13
range_summa = 0
hind = 0
range_kokku = 0




ev_data = [
    ['vehicle', 'range', 'price'],
    ['Tesla Model Y Long Range', '330', '58990'],
    ['Volkswagen ID.4 Pro', '260', '39995'],
    ['Ford Mustang Mach-E', '300', '42995'],
    ['Audi e-tron GT', '238', '102700'],
    ['Nissan Leaf', '149', '27400'],
    ['BMW iX xDrive50', '324', '83995'],
    ['Polestar 2', '265', '45500'],
    ['Kia EV6 Long Range', '310', '47795'],
    ['Mercedes-Benz EQS 450+', '350', '102310'],
    ['Hyundai Kona Electric', '258', '37400']
]

for i in ev_data:
    print(f"{i[0]:26} {i [1]:6} {i[2]:8}")

for i in range(1,len(ev_data)):
    range_summa+=int(ev_data[i][1])
    hind+int(ev_data[i][2])
    range_kokku+=1
    if int(ev_data[i][1]) > 300:
        print(ev_data[i][0])
        
    
    
print(f"Keskmine ulatus: {range_summa/range_kokku}")
print(f"Keskmine hind: {hind/range_kokku}")

print("---------------------")

max_koef = 1000000000
parim_auto = " "
for i in range(1,len(ev_data)):
    koef = int(ev_data[i][2]/int(ev_data[i][1]))
    if koef<max_koef:
        max_koef = koef
        parim_auto = ev_data[i][2]
    print(max_koef)
    print(parim_auto)



