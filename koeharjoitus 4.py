#1
import random

luku = int(input("Montako arpakuutiota heitetään? "))

summa = 0

for i in range(luku):
    heitto = random.randint(1,6)
    summa += heitto

print("Silmälukujen summa on ", summa)

#2

lista = []

while True:
    luku = input("Anna luku: ")

    if luku == "":
        break

    luku2 = int(luku)
    lista.append(luku2)

lista.sort(reverse=True)

print("Viisi suurinta:", lista[:5])


#3

lista = []

for i in range(5):
    nimi = input("Anna kaupungin nimi: ")
    lista.append(nimi)
for i in lista:
    print(i)


#4

summa = 0

luku = int(input("Anna kokonaisluku: "))

for i in range(1, luku+1):
    print(i)
    summa += i

print("Lukujen summa on ", summa)


#5

lista = []

for i in range(1,7):
    nimi = input("Anna nimi: ")
    lista.append(nimi)

lista.reverse()

for nimi in lista:
    print(nimi)


#6

luku = int(input("Anna kokonaisluku: "))

print(luku*1)
print(luku*2)
print(luku*3)
print(luku*4)
print(luku*5)
print(luku*6)
print(luku*7)
print(luku*8)
print(luku*9)
print(luku*10)




