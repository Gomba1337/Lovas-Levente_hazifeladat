import random

oszlopok = ["A", "B", "C"]
sorok = ["1", "2", "3"]

hajo_oszlop = random.choice(oszlopok)
hajo_sor = random.choice(sorok)
cel = hajo_oszlop + hajo_sor

probalkozasok = 0
talalat = False


print("Torpedó játék (3x3)")
print("A pozíciók: A1, A2, A3, B1, B2, B3, C1, C2, C3")
print("Találja el a hajót!")


while not talalat:
    tipp = input("Kérem a tippet: ").upper()
    probalkozasok += 1
    
    if len(tipp) != 2 or tipp[0] not in oszlopok or tipp[1] not in sorok:
        print("Próbálja újra.")
        probalkozasok -= 1
        continue

    if tipp == cel:
        print(f"Eltaláltad! A hajó a {cel} pozíción volt.")
        talalat = True
    else:
        print("Nem talált, próbálja újra!")

print(f"Gratulálok!!")
print(f"A feladat{probalkozasok} próbálkozásból sikerült.")
