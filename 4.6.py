def kuu_nimi(list):
    kuu = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", 
            "juuli", "august", "september", "oktoober", "november", "detsember"]
    return kuu[list - 1]
def kuupaev_sonena(kuupaev):
    
    i = kuupaev.split(".")
    paev = i[0]
    kuu = int(i[1])
    aasta = i[2]

    tekst = kuu_nimi(kuu)
    return (f"{paev}. {tekst} {aasta}. a")

kujundus = input("Sisesta kuupaeva kujul DD.MM.YYYY: ")
kokku = kuupaev_sonena(kujundus)
print(kokku)