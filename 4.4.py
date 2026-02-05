def tervitus(j):
    print('Võõrustaja: "Tere!"')
    print(f'Täna {j}. kord tervitada, mõtiskleb võõrustaja.')
    print('Külaline: "Tere, suur tänu kutse eest!"')

arv = int(input("Sisestage külaliste arv: "))

for i in range(1, arv + 1):
    tervitus(i)