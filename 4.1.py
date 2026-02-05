def banner(text):
    return text.upper()

f = input("Sisesta reklaamtekst: ")

kordused = int(input("Mitu korda kuvada: "))

for i in range(kordused):
    print(banner(f))
