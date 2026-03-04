#1 tehtävä

nimi = input("Kerro nimesi:")


if nimi == "Matti":
    print("Seuraava kiitos!")
else :
    maara = float(input("Montako keittoannosta?"))
    print("Kokonaishinta on", maara * 5.90)


#2 tehtävä

palkka = float(input("Kerro tuntipalkkasi:"))
tunnit = float(input("Montako tuntia olet tehnyt?"))
paiva = input("Mikä viikonpäivä?")

if paiva == "sunnuntai":
    print("Päiväpalkkasi on", palkka * tunnit * 2)
else:
    print("Päiväpalkkasi on", palkka * tunnit)


#3 tehtävä

from math import sqrt

while True:
    luku = int(input("Anna kokonaisluku:"))

    if luku < 0:
        print("Virheellinen numero.")
    elif luku > 0:
        print("Lukusi neliojuuri on", sqrt(luku))
    else:
        print("Exiting...")
        break



#4 tehtävä

tarina = ""
edellinen = ""

while True:
    sana = input("Anna sana lisättäväksi tarinaan:")

    if sana == "Loppu" or sana == edellinen:
        break

    tarina += sana + " "
    edellinen = sana

print(tarina)


#5 tehtävä

import math

while True:
    lasku = input("Valitse laskutoimitus. (Loppu lopettaa ohjelma)")

    if lasku == "Loppu":
        break

    luku1 = float(input("Anna ensimmäinen luku:"))
    luku2 = float(input("Anna toinen luku:"))


    if lasku == "Yhteenlasku":
        print("Lukujesi yhteenlaskun tulos on", luku1 + luku2)
    elif lasku == "Vähennyslasku":
        print("Lukujesi vähennyslaskun tulos on", luku1 - luku2)
    elif lasku == "Kertolasku":
        print("Lukujesi kertolaskun tulos on", luku1 * luku2)
    elif lasku == "Jakolasku":
        print("Lukujesi jakolaskun tulos on", luku1 / luku2)


