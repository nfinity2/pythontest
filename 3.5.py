from datetime import*

failinimi = input("Sisesta failinimi: ")

paev = datetime.now().day
print(f"Täna on {paev}. kuupäev")

fail = open("nimekiri.txt", "r", encoding="utf-8")

nimed = []
for rida in fail:
    nimed.append(rida.strip())

fail.close

arv_vastajaid = 1
print("Täna peab vastama")
for i in range(arv_vastajaid):
    koht = (paev + i) % len(nimed)
    print(f"{i + 1.}. {nimed[koht]}")