szamok = []

print("Adjon meg számokat.")

while True:
    be = input("Kérek egy számot: ")
    
    if be == "x" or be == "X":
        break
        
    try:
        szam = int(be)
        szamok.append(szam)
    except ValueError:
        print("Érvénytelen szám")

paros_szamok = []
for szam in szamok:
    if szam % 2 == 0:
        paros_szamok.append(szam)

print(f"A megadott számok: {szamok}")

if paros_szamok:
    print(f"A páros számok: {paros_szamok}"
    f"A legkisebb páros szám: {min(paros_szamok)}"
    f"A legnagyobb páros szám: {max(paros_szamok)}")
else:
    print("Nem adott meg egy páros számot sem.")