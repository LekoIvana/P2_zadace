"parni"
def parni_brojevi(a):
    for i in range(a):
        if i%2 == 0:
            yield i

"neparni"           
def neparni_brojevi(a):
    for i in range(a):
        if i%2 == 0:
            yield i

broj = int(input("Unesite neki broj:"))


g_parnih = parni_brojevi(broj)
g_neparnih = neparni_brojevi(broj)

brojevi = zip(g_parnih, g_neparnih)

print("Parni:         Neparni:")

for parni, neparni in brojevi:
    print(" ", parni, " ", neparni)