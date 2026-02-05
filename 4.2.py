def mahlapakk_arv(ounte_kogus):
    arv = ounte_kogus * 0.4 / 3
    return round(arv)

ounte_kogus = float(input("Sisesta oma õuna kogus"))
mahlapakk = mahlapakk_arv(ounte_kogus)

print(mahlapakk)