import random

lista = []
for x in range(5):
    szam = random.randint(1, 10)
    lista.append(szam)

összeg = sum(lista)

print(f"A lista elemei: {lista}")
print(f"A számok összege: {összeg}")

