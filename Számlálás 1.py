import random


lista = []
for _ in range(5):
    szam = random.randint(1, 10)
    lista.append(szam)

páros_db = 0
for szam in lista:
    if szam % 2 == 0:
        paros_db += 1

print(f"A lista elemei: {lista}")
print(f"A listában {páros_db} darab páros szám van.")