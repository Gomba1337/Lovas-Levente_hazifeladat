import random

lista = []
for _ in range(5):
    szam = random.randint(1, 7)
    lista.append(szam)

print(f"A generált lista: {lista}")

szam = int(input("Adjon meg egy számot 1 és 7 között: "))
    
if szam in lista:
        print(f"A {szam} szerepel a listában.")
else:
        print(f"A {szam} nem szerepel a listában.")
