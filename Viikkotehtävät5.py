#1 tehtävä

import random

luku = int(input("Kuinka monta arpakuutiota heitetään?"))

summa = 0

for i in range(luku):
    silmaluku = random.randint(1, 6)
    print("Arpakuutio", i + 1, ":", silmaluku)
    summa += silmaluku

print("Silmälukujen summa on", summa)

#2 tehtävä

luvut = []

while True:
    luku = input("Anna luku (tyhjä lopettaa merkkijonon):")

    if luku == "":
        break

    luvut.append(int(luku))

luvut.sort(reverse=True)

print("Viisi suurinta lukua:")
for luku in luvut[:5]:
    print(luku)

#3 tehtävä

luku = int(input("Anna kokonaisluku:"))

on_alkuluku = True

if luku < 2:
    on_alkuluku = False
else:
    for i in range(2, luku):
        if luku % i == 0:
            on_alkuluku = False
            break

if on_alkuluku:
    print("Luku on alkuluku")
else:
    print("Luku ei ole alkuluku")


#4 tehtävä

kaupungit = []

for i in range(5):
    nimi = input("Anna viiden kaupungin nimet yksitellen.")
    kaupungit.append(nimi)

print("Kaupungit järjestyksessä:")

for kaupunki in kaupungit:
    print(kaupunki)