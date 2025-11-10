szavak = ["Eger", "körte", "elem", "eper", "dinnye"]
találatok = []
db = 0

for szo in szavak:
    if "e" in szo or "E" in szo:
        db += 1
        találatok.append(szo)

print(f"A listában {db} darab 'e' vagy 'E' betűt tartalmazó szó van.")
print("Ezek száma:")
for szo in találatok:
    print(szo)
