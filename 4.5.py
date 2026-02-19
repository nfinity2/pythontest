def pronksikarva_summa(tarv):
    summa = 0
    for arv in tarv:
        if arv == 1 or arv == 2 or arv == 5:
            summa += arv
    return summa

failinimi = input("Palun sisesta failinimi!: ")

fail = open("munt.txt",encoding="utf-8")

tarv = []
for rida in fail:
    arv = int(rida.strip())
    tarv.append(arv)

fail.close()

tulemus = pronksikarva_summa(tarv)

print(f"Hoiupõrsaasse läheb {tulemus} senti.")