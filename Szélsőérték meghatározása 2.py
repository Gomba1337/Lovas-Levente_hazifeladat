szavak = []

print("Adjon meg szavakat.")

while True:
    szo = input("Kérek egy szót: ")
    
    if not szo:
        break
    
    szavak.append(szo)

if szavak:
    print(f"A megadott szavak: {szavak}")
    
    legrovidebb = szavak[0]
    leghosszabb = szavak[0]
    
    for szo in szavak:
        if len(szo) < len(legrovidebb):
            legrovidebb = szo
        if len(szo) > len(leghosszabb):
            leghosszabb = szo
            
    print(f"A legrövidebb szó: {legrovidebb}"
   f"A leghosszabb szó: {leghosszabb}")
else:
    print("Nem adott meg egy szót sem.")