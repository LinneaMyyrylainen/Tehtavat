#1

yritykset = 0

while yritykset < 3:
    koodi = int(input("Anna PIN-koodi: "))

    if koodi == 1234:
        print("Oikein!")
        break
    else:
        print("Väärin.")
        yritykset += 1

    if yritykset == 3:
        print("Kortti lukittu")



#2

summa = 0

while True:
    luku = int(input("Anna luku (negatiivinen lopettaa): "))

    if luku < 0:
        break
    summa += luku

print("Lukujen summa on", summa)

#3

while True:
    sana = input("Anna salasana: ")

    if len(sana) >= 8:
        print("Hyväksytty.")
        break
    else:
        print("Salasana liian lyhyt.")

#4

import math

summa = 0
maara = 0

while True:
    luku = int(input("Anna luku: "))

    if luku == 0:
        break
    summa += luku
    maara += 1


print("Lukujen keskiarvo on ", summa / maara )


#5

luku1 = int(input("Anna ensimmäinen luku: "))
luku2 = int(input("Anna toinen luku: "))
luku3 = int(input("Anna kolmas luku: "))

if luku1 > 0 and luku2 > 0 and luku3 > 0:
    print("OK")
else:
    print("Virhe.")


#6

while True:
    sana = input("Anna sana: ")
    if sana == "":
        print("Ohjelma loppuu...")
        break
    print("Sanassa on",len(sana), "kirjainta.")


