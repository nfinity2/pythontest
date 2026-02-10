# Ülesanne 12

#     Loo funktsioon, mis võimaldab kasutajal teisendada temperatuuri Celsiusest Fahrenheitiks ja vastupidi.
#     Funktsioon võtab kaks argumenti: temperatuuri väärtuse ja teisendamise suuna, kus ‘C’ tähendab Celsiusest Fahrenheitiks teisendamist ja ‘F’ vastupidi.
#     Vaikimisi on teisendamise suund Celsiusest Fahrenheitiks.
#     Funktsiooni peab kaasnema selge dokumentatsioon, mis kirjeldab selle ülesannet, parameetreid ja mida tagastab.
#     Implementeeri loogika temperatuuri teisendamiseks kasutades vastavaid valemeid:

def temp(t,v):
    """
    Teisenda C-> F Või F-> C
    Parameetrid:
    t (int): Kraadid.
    v (string): Vali teisendus F või C

    Tagastab:
    string: Tagastab teisednuse või veateate

    Näide:
    print(temp(20,"C"))
    -6,66
    """
    if v =="F":
        vastus = t * 9/5 + 32 
    elif v=="C":
        vastus = (t - 32) / (9/5)
    else:
        vastus="Vale sisestus"

    return vastus

print(temp(20,"C"))
print(temp(20,"F"))
print(temp(20,"Cddd"))
print(temp.__doc__)


# 200/100*10

kytus = lambda kytusekulu, vahemaa: (vahemaa/100) * kytusekulu
print(kytus(10, 200))



konto = 500

def depo(raha, konto):
    """
    Suureparanae maidla elab siin koodis kusagil
    """    
    summa = konto+raha
    return summa

def valja(raha, konto):
    """
    Suureparanae maidla elab siin koodis kusagil
    """
    summa = konto - raha
    return summa

konto = depo(10, konto)
konto = depo(130, konto)
konto = depo(51, konto)
konto = valja(1500, konto)
konto = depo(398, konto)
konto = depo(217, konto)


print(depo.__doc__)
print("Kontoseis: ", konto)
