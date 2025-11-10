szavak = ["asztal", "Alacska", "autó", "ablak",]
találatok = []
db = 0

for szo in szavak:
    if szo.startswith("a") or szo.startswith("A"):
        db += 1
        találatok.append(szo)


print(f"A listában {db} darab 'a' vagy 'A' betűvel kezdődő szó van.")
print("Ezek a következők:")
for szo in találatok:
    print(szo)