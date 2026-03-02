#1 tehtävä

luku = 1

while luku <= 1000:
    if luku % 3 == 0:
        print(luku)
    luku += 1

#2 tehtävä


while True:
    tuumat = float(input("Anna tuumamäärä (negatiivinen luku lopettaa): "))

    if tuumat < 0:
        break

    senttimetrit = tuumat * 2.54
    print( tuumat, "tuumaa on" , senttimetrit, "cm")

print("Ohjelma lopetetaan.")


#3 tehtävä

ensimmainen = 1

while True:
    teksti = input("Anna lukuja (Enter lopettaa merkkijonon): ")

    if teksti == "":
        break

    luku = float(teksti)

    if ensimmainen == 1:
            pienin = luku
            suurin = luku
            ensimmainen = 0
    else:
            if luku < pienin:
                pienin = luku
            elif luku > suurin:
                suurin = luku

if ensimmainen == 0:
    print("Pienin luku on", pienin)
    print("Suurin luku on", suurin)


#4 tehtävä


import random

luku = random.randint(1, 10)

while True:
    arvaus = int(input("Arvaa luku väliltä 1-10."))

    if arvaus > luku:
        print("Liian suuri arvaus.")
    elif arvaus < luku:
        print("Liian pieni arvaus.")
    else:
        print("Oikein!")
        break


#5 tehtävä

yritykset = 0

while yritykset < 5:
    tunnus = input("Anna käyttäjätunnus:")
    salasana = input("Anna salasana:")

    if tunnus == "python" and salasana == "rules":
        print("Tervetuloa")
        break
    else:
        yritykset = yritykset + 1

if yritykset == 5:
    print("Pääsy evätty.")

