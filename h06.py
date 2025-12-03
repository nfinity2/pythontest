# Ülesanne 05
# Armin 26.11.2025


#5.3 Matemaatika test
import random

arv1 = random.randint(1,10)
arv2 = random.randint(1,10)
vastus = int(input(f"{arv1} * {arv2}"))
if vastus == arv1 *  arv2:
    print("Õige!")
else:
    print("Vale!")







#5.1 Vanusepiiranguga üritus
piirang = 18
vanus = int(input("Siseta vanus: "))

if vanus > piirang:
    print("Sa saad sisse!")
else:
    print("Sa ei saa sisse!")
