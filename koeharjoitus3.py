#1

i = 1

while i <= 1000:
    if i % 3 == 0:
        print(i)
    i += 1

#2


while True:

    luku = float(input("Anna luku, jonka haluat muuttaa senttimetreiksi (negatiivinen lopettaa): "))

    if luku <= 0:
        print("Ohjelma loppuu...")
        break
    else:
        print(luku, "on", luku*2.54, "senttimetriä")

#4

import random
luku = random.randint(1,10)

while True:

    kysymys = int(input("Arvaa luku: "))

    if kysymys == luku:
        print("Oikein!")
        break
    elif kysymys > luku:
        print("Luku on pienempi")
    elif kysymys < luku:
        print("Luku on suurempi")


#5

yritykset = 0


while yritykset < 5:
    tunnus = input("Anna käyttäjätunnus: ")
    salasana = input("Anna salasana: ")

    if tunnus == "python" and salasana == "rules":
        print("Tervetuloa!")
        break
    else:
        yritykset += 1
        print("Yritä uudelleen")


if yritykset == 5:
    print("Pääsy evätty.")


#6

summa = 0

while True:

    luku = int(input("Anna luku (0 lopettaa):"))

    if luku == 0:
        print("Annoit yhteensä", summa, "parillista lukua.")
        break
    elif luku % 2 == 0:
        summa += 1


#7

import random

yritykset = 0
luku = random.randint(1,10)

while yritykset < 5:
    arvaus = int(input("Arvaa luku:"))


    if arvaus == luku:
        print("Voitit!")
        break
    else:
        print("Väärin.")

    yritykset += 1

if yritykset == 5:
    print("Hävisit...")

