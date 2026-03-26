#1 tehtävä

luku = int(input("Anna luku:"))
print("Antamasi luvun kertotaulu 1-10.")

for i in range(0,11):
    print(luku * i)

#2 tehtävä

lista = []


while True:
    luku = int(input("Anna luku, joka lisätään listaan:"))

    if luku == 0:
        print("Hei Hei!")
        break
    lista.append(luku)
    print("Lista nyt:", lista)
    print("Lista järjestyksessä:", sorted(lista))

#3 tehtävä

lista = ["koira", "kissa", "leipä", "voi", "kana", "puu", "pöytä", "leivänpaahdin","koirankoppi"]

laskuri = 0

for sana in lista:
    if len(sana) > 5:
        laskuri += 1

print("Yli 5 kirjainta on sanoissa:", laskuri)

#4 tehtävä

def kuusi(koko):
    print("Tämä on kuusi!")

    for i in range(1, koko + 1):
        print( " " * (koko-i) + "*" * (2 * i - 1))


    print( " " * (koko - 1) + "*")

kuusi(5)

#5 tehtävä

def suurin_arvo(a, b, c):
    return max(a, b, c)

luku1 = int(input("Anna ensimmäinen luku:"))
luku2 = int(input("Anna toinen luku:"))
luku3 = int(input("Anna kolmas luku:"))

suurin = suurin_arvo(luku1, luku2, luku3)

print("Suurin arvo on:", suurin)

#6 tehtävä


#6 tehtävä

import math

def summa(a,b):
    return a + b
def erotus(a,b):
    return a - b
def tulo(a,b):
    return a * b
def jako(a,b):
    if b == 0:
        return "Ei voi jakaa nollalla"
    return a / b


while True:
    lasku = input("Valitse laskutoimitus (Yhteenlasku, Vähennyslasku, Jakolasku tai Kertolasku), loppu lopettaa ohjelman.")

    if lasku == "Loppu":
        break

    luku1 = float(input("Anna ensimmäinen luku:"))
    luku2 = float(input("Anna toinen luku:"))


    if lasku == "Yhteenlasku":
        print("Lukujesi yhteenlaskun tulos on", summa(luku1, luku2))
    elif lasku == "Vähennyslasku":
        print("Lukujesi vähennyslaskun tulos on", erotus(luku1, luku2))
    elif lasku == "Kertolasku":
        print("Lukujesi kertolaskun tulos on", tulo(luku1, luku2))
    elif lasku == "Jakolasku":
        print("Lukujesi jakolaskun tulos on", jako(luku1, luku2))
