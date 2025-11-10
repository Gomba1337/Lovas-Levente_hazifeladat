import random

szavak = ["alma", "körte", "szilva", "barack", "banán"]
szo = random.choice(szavak)
jo_tippek = []
rossz_tippek = []

print(f"Gondoltam egy gyümölcsre. Találd ki, milyen betűk vannak benne!")
print("A kilépéshez nyomd meg az enter-t.")


while True:
    print("-" * 20)
    
    jelenlegi_allas = "_"
    for betu in szo:
        if betu in jo_tippek:
            jelenlegi_allas += betu
        else:
            jelenlegi_allas += "_"
    
    print(f"A szó: {jelenlegi_allas}"
    f"Jó tippek: {jo_tippek}"
    f"Rossz tippek: {rossz_tippek}")
    

    tipp = input("Mi a következő tipp? ").lower()
    
    if not tipp:
        print("Kilépés")
        break
        
    if len(tipp) > 1:
        print("Csak egy betűt adjon meg!")
        continue

    if tipp in szo:
        if tipp not in jo_tippek:
            print("Eltaláltad!")
            jo_tippek.append(tipp)
        else:
            print("Ezt már volt és rossz volt")
    else:
        if tipp not in rossz_tippek:
            print("Sajnos nem találtad el")
            rossz_tippek.append(tipp)
        else:
            print("Ezt már tippelted és rossz volt")
            
    if all(betu in jo_tippek for betu in szo):
        print(f"Kitaláltad a szót: {szo}")
        break

if not all(betu in jo_tippek for betu in szo):
    print(f"Vége:)"
    f"A kitalálandó szó a '{szo}' volt")