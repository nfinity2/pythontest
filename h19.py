import csv

faili_nimi = 'EstonianBasketballGames.csv'
meeskonnad_kokku = {}

with open(faili_nimi, mode='r', encoding='utf-8') as fail:
    csv_lugeja = csv.reader(fail)

    pais = next(csv_lugeja)

    print(f"Päise veerud: {pais}")
    for rida in csv_lugeja:
        if (rida[1]) not in meeskonnad_kokku:
            meeskonnad_kokku.append(rida[1])
        if (rida[2]) not in meeskonnad_kokku:
            meeskonnad_kokku.append(rida[2])

print(f"Meeskonnad kokku: {len(meeskonnad_kokku)}")