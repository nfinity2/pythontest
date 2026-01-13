# tee koik for-tsukliga
#Grupp1 10.1


i = int(input("Mitu arvu sisestad?"))
summa = 0
for j in range(i):
    arv = float(input(f"Siseta arv {j + 1}: "))
    summa += arv
    
keskmine = summa / i
print("Arvude keskmine arv on:", keskmine)