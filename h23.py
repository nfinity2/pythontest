# from datetime import date, datetime, timedelta


# # Lihtne kuupäev
# # Kuva praegune päev, kuu, aasta, tund, minut
# now = datetime.now()
# print (now)
# # Vorminda praegune kuupäev järgmiselt: d.m Y,  H:M:S
# print(now.strftime("%d.%m %Y,  %H:%M:%S"))
# # Lisa oma sünniaeg, arvuta ja kuva, mitu päeva vana oled'
# sp = datetime(2008,11,6)
# vanus_paevades = now - sp
# print(f"Vanus päevades {vanus_paevades}")
# # Kuva vanus aastates
# vanus_aastates = vanus_paevades.days // 365
# print(f"Vanus aastates {vanus_aastates}")
# # Kuva, kas tegemist on juubeliaastaga
# if vanus_aastates%5 == 0:
#     print("juubel")
# else:
#     print("mu nimi kevin")


# Autorent
# Kasuta seda faili: rentals.csv
# Rendite arv – leia mitu ronditehingut on tehtud
# Unikaalsed kliendid ja keskmine vanus – arvutage, mitu unikaalset klienti (customer ID) andmetes esineb ja mis on teie klientide keskmine vanus
# Tagastamine – milline osakaal broneeringutest hõlmab risti-kontori rentimist, kus klient võtab auto ühest kohast ja tagastab selle teise kontorisse?
# Keskmine rentimise kestus – mis on keskmine rentimise kestus?

import csv

rentite_arv = 0
cid = []

faili_nimi = 'rentals.csv'
with open(faili_nimi, mode='r', encoding='utf-8') as fail:
    csv_lugeja = csv.reader(fail)

    pais = next(csv_lugeja)

    for rida in csv_lugeja:
        rentite_arv+=1
        print(rida[7])
    if rida[7] not in cid:
        cid.append(rida[7])

print(f"rentite arv on {rentite_arv}")
print(f"pede arv on {len(cid)}")
