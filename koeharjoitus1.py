#1
import random

print("Hei maailma!")

#2

nimi = input("Mikä on nimesi? ")
print("Hei, ",nimi)

#3

luku1 = float(input("Anna ensimmäinen luku: "))
luku2 = float(input("Anna toinen luku: "))

print("Lukujen summa on: ", luku1 + luku2)

#4

luku = int(input("Anna kokonaisluku: "))

if luku % 2 == 0:
    print("Lukusi on parillinen.")
else:
    print("Lukusi on pariton.")

#5

sana = input("Anna sana: ")
numero = int(input("Anna numero: "))

for i in range(numero):
    print(sana)

#6

luku1 = float(input("Anna ensimmäinen luku: "))
luku2 = float(input("Anna toinen luku: "))
lasku = input("Minkä laskutoimituksen haluat suorittaa? (+, -, *, /)")

if lasku == "+":
    print("Lukujen summa on: ", luku1 + luku2)
elif lasku == "-":
    print("Lukujen erotus on: ", luku1 - luku2)
elif lasku == "*":
    print("Lukujen kertolaskun tulos on: ", luku1 * luku2)
elif lasku == "/":
    print("Lukujen jakolaskun tulos on: ", luku1 / luku2)
else:
    print("Virheellinen syöte.")

#7

luku1 = float(input("Anna ensimmäinen luku: "))
luku2 = float(input("Anna toinen luku: "))

if luku1 < luku2:
    print(luku2, "on suurempi kuin", luku1)
elif luku1 > luku2:
    print(luku1, "on suurempi kuin", luku2)
else:
    print("Virheellinen syöte.")

#8

luku1 = float(input("Anna ensimmäinen luku: "))
luku2 = float(input("Anna toinen luku: "))
luku3 = float(input("Anna kolmas luku: "))

print("Lukujen keskiarvo on", (luku1 + luku2 + luku3)/3)

#9

for i in range(1, 11):
    print(i)

#10

summa = 0

for i in range(1, 101):
    summa = summa + 1

print("Lukujen summa on: ", summa)

#11

import random

oikea = random.randint(1, 10)
arvaus = int(input("Arvaa luku: "))

while True:
    if oikea == arvaus:
        print("Luku on oikein.")
        break
    elif oikea > arvaus:
        print("Liian pieni")
    elif oikea < arvaus:
        print("Liian suuri.")

    arvaus = int(input("Arvaa uudestaan: "))


#12

luku = int(input("Anna luku, jonka kertotaulun haluat (1-10): "))

print(luku)
print(luku * 2)
print(luku * 3)
print(luku * 4)
print(luku * 5)
print(luku * 6)
print(luku * 7)
print(luku * 8)
print(luku * 9)
print(luku * 10)

#13

sana = input("Anna sana: ")
pituus = len(sana)

print("Sanassasi on", pituus, "kirjainta.")

#14



while True:
    sana = input("Anna salasana: ")
    if sana == "python123":
        print("Salasana oikein.")
        break
    else:
        print("Salasana väärin.")
        print("Arvaa uudestaan.")


#15
import math

sade = float(input("Anna ympyrän säde: "))

print("Ympyrän pinta-ala on: ", sade**2 * math.pi )

#16

import random

luku1 = random.randint(0,9)
luku2 = random.randint(0,9)
luku3 = random.randint(0,9)

print(luku1, luku2, luku3)

#17

kanta = float(input("Anna suorakulmion kanta: "))
korkeus = float(input("Anna suorakulmion korkeus: "))

print("Suorakulmion piiri on: ", 2*kanta + 2*korkeus)
print("Suorakulmion pinta-ala on: ", kanta * korkeus)





