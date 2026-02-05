muusika = int(input("1) EDM 2) 80-ndad 3) Eesti Muusika 4) Jukebox "))
 
if muusika == 2:
    failinimi = "80ndad.txt"
elif muusika == 3:
    failinimi = "eesti_muusika.txt"
else:
    failinimi = "jukebox.txt"

fail = open(failinimi, "r", encoding="utf-8")

arv = 1
for rida in fail:
    rida = rida.strip() 
    print(f"{arv}. {rida}")
    arv=arv + 1 

valik = int(input("Valige laulu järjekorranumber"))

fail.seek(0)

arv = 1 
for rida in fail:
    if arv == valik: 
        print(rida)
    arv += 1
fail.close()
