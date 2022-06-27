import random

imena = ['John', 'Scott', 'Bonita', 'Marjorie', 'Mary', 'Craig', 'Colleen', 'Luis', 'Lloyd', 'Steven', 'Mildred', 'Glen', 'Willie', 'Jesse', 'Diane', 'Frank', 'Jared', 'Sheri', 'Margaret', 'Victoria']

ukupno_studenata = len(imena)

broj_studenata = {}


for ime in imena:
    broj_studenata[ime] = 0

for ime in imena:
    if ime in broj_studenata:
        broj_studenata[ime] += 1
    
    else:
        broj_studenata[ime] = 1



studenti_posebno = []
kljucevi = broj_studenata.keys()
for ime in kljucevi:
    studenti_posebno.append(ime)

ocjene = {}

jedinice = 0
dvice = 0
trice = 0
cetvrtice = 0
petice = 0
pozitivno = 0 

for ime in studenti_posebno:
    for i in range(broj_studenata(ime)):
        ocjene[ime+str(i+1)] = random.randint(1, 5) 
        if ocjene[ime +str(i+1)] > 1:
            pozitivno += 1
        if ocjene[ime +str(i+1)] == 1:
            jedinice += 1
        elif ocjene[ime +str(i+1)] == 2:
            dvice += 1
        elif ocjene[ime +str(i+1)] == 3:
            trice += 1
        elif ocjene[ime +str(i+1)] == 4:
            cetvrtice += 1
        else:
            petice += 1

parovi = ocjene.items()


for ime, ocjena in parovi:
    print(ime, "=", ocjena)

print("Prošlo je:", (pozitivno/ukupno_studenata)*100, "%")
print("Jedinice:", jedinice)
print("Dvice:", dvice)
print("Trice:", trice)
print("Cetvrtice:", cetvrtice)
print("Petice:", petice)











