számok = []

összeg = 0

print("Adjon meg egész számokat [-5;5] intervallumban.")
print("A program leáll, ha intervallumon kívüli számot ad meg.")

while True:
    try:
        be = input("Kérek egy számot: ")
        szám = int(be)
        
        if -5 <= szám <= 5:
            számok.append(szám)
            összegsszeg += szám
        else:
            print("Ez a szám intervallumon kívüli, a bekérés leáll.")
            break
            
    except ValueError:
        print("Ez nem volt érvényes egész szám, próbálja újra.")


print(f"A megadott intervallumba eső számok: {számok}")
print(f"Ezek összege: {összeg}")