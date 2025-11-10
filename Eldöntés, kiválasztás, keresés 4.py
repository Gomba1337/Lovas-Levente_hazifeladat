szoveg = input("Adjon meg egy szöveget: ").lower()

maganhangzok = "aáeéiíoóöőuúüű"


print("Eredmények")

for mgh in maganhangzok:
    db = 0
    helyek = []
    
    for index, betu in enumerate(szoveg):
        if betu == mgh:
            db += 1
            helyek.append(str(index + 1))
            
    if db > 0:
        print(f"A '{mgh}' magánhangzó előfordult a szövegben."
        f"  Darabszám: {db}"
       f"  Hely: {', '.join(helyek)}")
    else:
        print(f"A '{mgh}' magánhangzó nem fordult elő a szövegben.")
        
    print("-" * 20)