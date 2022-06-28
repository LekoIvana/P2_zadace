import re
 
regex = "^i[0-5]+\s.*l$"

while True:
    unos = input("unesite ime:")
    provjera = re.match(regex,unos)
    if provjera:
        break
    else:
        print("pogresan unos!")

print("uspjesno!")
