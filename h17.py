import os
from datetime import date

print("Tere", os.getlogin())
print(os.getcwd())
mitu = int(input("Mitu kataloogi tahad: "))
today = str(date.today())
try:
    os.mkdir("uus_kaust")
    for i in range(mitu):
        os.mkdir(today+"/"+str(i+1))
except FileExistsError:
    print(f"Kataloog {today} juba eksisteerib.")

