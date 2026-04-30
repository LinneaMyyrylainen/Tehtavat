#1

def tervehdys():
    print("Hei maailma!")

tervehdys()

#2

def tervehdys2(nimi):
    print("Hei", nimi)
    return

tervehdys2("Ella")

#3

def summa(a, b):
    return a+b

tulos = summa(1, 2)
print(tulos)

def kerto(a, b):
    return(a*b)

tulos2 = kerto(3,6)
print(tulos2)


#4

lista = [1,2,3,4,5,6]

def summa(lista):
    return sum(lista)

print(summa(lista) / len(lista))

#5

import random

def noppa():
    return random.randint(1,6)

while True:
    tulos = noppa()
    print(tulos)

    if tulos == 6:
        break


#6

import random

def noppa(tahkot):
    return random.randint(1, tahkot)

tahkot = int(input("Anna nopan tahkojen määrä: "))

while True:
    tulos = noppa(tahkot)
    print("Heitto:", tulos)

    if tulos == tahkot:
        break


#7

def litra(gallona):
    return gallona*3.785

while True:
    gallona = float(input("Anna gallonamäärä: "))

    if gallona < 0:
        print("Ohjelma loppuu...")
        break

    print(gallona, "gallonaa on ", litra(gallona), "litraa.")
