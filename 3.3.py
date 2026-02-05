fail = open("konto.txt")
for rida in fail:
    arv = float(rida)
    if arv > 0:
        print(arv)

fail.close()