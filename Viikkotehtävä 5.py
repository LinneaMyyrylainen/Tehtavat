#1 tehtävä

import random

maara = int(input("Kuinka monta arpakuutiota heitetään?"))

summa = 0

for x in range(maara):
    heitto = random.randint(1,6)
    summa += heitto

print("Silmälukujen summa on", summa)


#2 tehtävä



#3 tehtävä

luku = int(input("Anna luku:"))

if luku / luku == 1:
    if luku / 1 == luku:
        print("Antamasi luku on alkuluku.")
else:
    print("Antamasi luku ei ole alkuluku.")



luku = int(input("Anna luku (Enter lopettaa merkkijonon)"))