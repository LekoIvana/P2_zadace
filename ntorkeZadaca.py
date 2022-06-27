def ocjena(bodovi):
    if bodovi < 50:
        return "nedovoljan"
    elif bodovi < 65:
        return "dovoljan"
    elif bodovi < 80:
        return "dobar"
    elif bodovi < 90:
        return "vrlo dobar"
    else:
        return "odličan"



from csv import reader
dat_rez = open("rezultati.csv", "r")
csv_reader = reader(dat_rez)



rezultati = list(map(tuple, csv_reader))



novirezultati = []
for ime, prezime, bodovi in rezultati:
    novirezultati.append((prezime, ime, bodovi))

#sortiramo
novirezultati.sort()

studenti = []

for student in novirezultati:
    rjecnik = {}
    rjecnik["prezime"] = student[0]
    rjecnik["ime"] = student[1]
    rjecnik["ocjena"] = ocjena(int(student[2]))
    studenti.append(rjecnik)


studentinovi = []

for student in studenti:
    studentinovi.append((student["prezime"], student["ime"], student["ocjena"]))

print("Novi popis studenata:",studentinovi) 
