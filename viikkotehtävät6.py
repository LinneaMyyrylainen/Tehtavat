#1 tehtävä
import random

def noppa():
    return random.randint(1,6)

luku = 0

while luku!=6:
    luku = noppa()
    print(luku)

#2 tehtävä

import random

def noppa(tahkot):
    return random.randint(1,tahkot)

maksimi = int(input("Anna nopan maksimisilmäluku:"))

luku = 0

while luku!=maksimi:
    luku = noppa(maksimi)
    print(luku)

#3 tehtävä

def gallonat_litroiksi(gallonat):
    return gallonat * 3.785

while True:

    maara = float(input("Anna bensiinimäärä gallonoina: "))

    if maara < 0:
        break
    litrat = gallonat_litroiksi(maara)
    print(litrat, "litraa")


#4 tehtävä

def laske_summa(lista):
    summa = 0
    for luku in lista:
        summa += luku
    return summa

luvut = [1,2,3,4,5]

tulos = laske_summa(luvut)
print("Summa on:", tulos)

#5 tehtävä

def  karsi_parittomat(lista):
    uusi_lista = []

    for luku in lista:
        if luku % 2 == 0:
            uusi_lista.append(luku)

    return uusi_lista

luvut = [1,2,3,4,5,6]

karsittu = karsi_parittomat(luvut)

print("Alkuperäinen lista:", luvut)
print("Karsittu lista:", karsittu)


#6 tehtävä

import math

def yksikkohinta(halkaisija, hinta):
    sade = halkaisija / 2
    pinta_ala = math.pi *sade**2
    return hinta/pinta_ala

h1 = float(input("Anna pizzan 1 halkaisija (cm):"))
p1 = float(input("Anna pizzan 1 hinta (€):"))

h2 = float(input("Anna pizzan 2 halkaisija (cm):"))
p2 = float(input("Anna pizzan 2 hinta (€):"))

y1 = yksikkohinta(h1, p1)
y2 = yksikkohinta(h2, p2)

print(f"Pizzan 1 yksikköhinta: {y1:.4f}€/cm")
print(f"Pizzan 2 yksikköhinta: {y2:.4f}€/cm")

if y1 < y2:
    print("Pizza 1 antaa enemmän vastinetta rahalle.")
elif y2 < y1:
    print("Pizza 2 antaa enemmän vastinetta rahalle.")
else:
    print("Pizzat ovat yhtä hyviä diilejä.")

