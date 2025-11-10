szo = "alma"
jo_tippek = []
rossz_tippek = []


print("Találd ki, milyen betűk vannak a szóban!")
print("A kilépéshez nyomd meg az enter-t.")


while True:
    print("-" * 20)
    print(f"Jó tippek: {jo_tippek}")
    print(f"Rossz tippek: {rossz_tippek}")
    
    tipp = input("Mi a következő tipp? ")
    
    if not tipp:
        print("Kilépés")
        break
        
    if len(tipp) > 1:
        print("Csak egy betűt adjon meg!")
        continue

    if tipp in szo:
        if tipp not in jo_tippek:
            print("Eltaláltad!!4!")
            jo_tippek.append(tipp)
        else:
            print("Ezt már tippelted és jó volt")
    else:
        if tipp not in rossz_tippek:
            print("Sajnos nem találtad el")
            rossz_tippek.append(tipp)
        else:
            print("Ezt már tippelted és rossz volt")


print("A játék véget ért.")
print(f"A kitalálandó szó a '{szo}' volt.")
