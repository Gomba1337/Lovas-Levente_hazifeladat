szamok = []
print("Adj meg számokat.")

while True:
    be = input("Kérek egy számot: ")
    
    if not be:
        break
        
    try:
        szam = int(be)
        szamok.append(szam)
    except ValueError:
        print("Nem érvényes szám.")

if szamok:
    print(f"A megadott számok: {szamok}"
   f"A legkisebb szám: {min(szamok)}"
    f"A legnagyobb szám: {max(szamok)}")
else:
    print("Nincs megadott szám")