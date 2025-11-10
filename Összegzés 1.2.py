import random


lista = []
for x in range(5):
    szam = random.randint(1, 10)
    lista.append(szam)

összeg = 0
for szam in lista:
    if szam % 2 == 0:
        osszeg += szam

print(f"A lista elemei: {lista}")
print(f"A páros számok összege: {összeg}")

