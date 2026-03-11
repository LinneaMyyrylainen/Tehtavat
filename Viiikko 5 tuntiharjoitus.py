#lista
from idlelib.config_key import WHITESPACE_KEYS

nimet = ["Viivi", "Ahmed", "Pekka", "Olga", "Mary"]
print(nimet)

#lisää listan loppuun
nimet.append("Matti")

#poistaa listasta
nimet.remove("Pekka")

#lisää listaan tiettyyn paikkaan
nimet.insert(4, "Matti")

print(nimet)

nimet2 = ["Allu", "Ninni"]

#lisää listan 2 listan 1 perään
nimet.extend(nimet2)
print(nimet)
print(nimet2)

#kertoo missä kohtaa tietty nimi on listassa
indeksi = nimet.index("Olga")

#kertoo onko haluttu nimi listassa vai ei
if "Matti" in nimet:
    print("Matti löytyi!")
else:
    print("Ei mattia!")

#järjestää nimet aakkosjärjestykseen
nimet.sort()
print(nimet)


#for-toistorakenne
#toistaa käskyn jokaiselle arvolle listassa

nimet = ["Viivi", "Ahmed", "Pekka", "Olga", "Mary"]
print(nimet)

for nimi in nimet:
    print("Tervehdys", nimi)

luvut = [14, 5, 6, 1, 0, 23]

summa = 0

for luku in luvut:
    summa += luku
    print("Tällä hetkellä summa on", summa)

print("Lopullinen summa on:", summa)


#range-funktio
#askelväli oletus 1 (ei tarvitse laittaa mitään)

luvut = list(range(1, 4))
print(luvut)

#askelväli -1 0 ei lasketa
lista = list(range(5, 0, -1))
print(lista)

#askelväli -2 0 ei lasketa
numerot = list(range(10, 0, -2))
print(numerot)


#harjoitus 1

list = ["Punainen", "Sininen", "Keltainen", "Vihreä", "Pinkki"]

vari = input("Mikä on lempivärisi?")

if vari in list:
    print("Värisi on listassa!")
else:
    print("Värisi ei ole listassa.")

#harjotus 2


list = ["Punainen", "Sininen", "Keltainen", "Vihreä", "Pinkki"]

vari = input("Mikä on lempivärisi?")

#Boolean muuttuja
loytyy = False

for v in list:
    if vari == v:
        #Boolean muuttuja muutetaan todeksi
        loytyy = True

if loytyy:
    print("Erinomainen valinta!")
else:
    print("Eksoottinen valinta!")


#harjoitus 2

ostoslista = ["maito", "juusto", "voi", "leipä"]

print("OSTOSLISTA:", ostoslista)
print("Mennään kauppaan... \n")

while ostoslista:
    ostos =input("Anna tuote, jonka ostit:")

    if ostos in ostoslista:
        ostoslista.remove(ostos)
        print("Jäljellä", ostoslista)
    else:
        print("Tuote ei ollut listallasi!")

print("Ostokset suoritettu!")



