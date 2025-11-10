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
        print("Ez nem volt érvényes szám (vagy 'x').")

if szamok:
    print(f"\nA megadott számok: {szamok}"
    f"A legkisebb szám: {min(szamok)}"
    f"A legnagyobb szám: {max(szamok)}")
else:
    print("\nNem adott meg egy számot sem.")
