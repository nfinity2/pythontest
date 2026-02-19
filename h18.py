tehingute_arv = 0
pos_tehing_arv = 0
pos_summa = 0

with open("pank.txt") as fail:
    for rida in fail:
        tehingute_arv+=1
        if float(rida.strip()) > 0:
            pos_tehing_arv+=1
            pos_summa+=float(rida.strip())
            print(rida.strip())
print(f"tehingute_arv: {tehingute_arv}")
print(f"pos tehingud: {pos_tehing_arv}")
print(f"summa: {pos_summa}")