ring = 6
porgand = 0

for i in range(ring):
    r = i+1
    if r % 2 == 0:
        porgand = porgand + r
print(porgand)
