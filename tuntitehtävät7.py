hedelmat = ("Päärynä", "Mango", "Ananas")

print(hedelmat)

h1, h2, h3 = hedelmat

print("Hedelmä 1 on", h1)
print("Hedelmä 2 on", h2)
print("Hedelmä 3 on", h3)


import random

def heitanoppia():
    n1 = random.randint(1,6)
    n2 = random.randint(1,6)
    return (n1,n2)

noppa1, noppa2 = heitanoppia()
print(f" Heitit ekasta nopasta {noppa1} ja tokasta nopasta {noppa2}, liiku siis {noppa1 +noppa2} askelta")


pelit = {"Kimble", "Uno", "Afrikantähti"}
print(pelit)

pelit.add("Minecraft")
pelit.remove("Kimble")

for p in pelit:
    print(p)



arvosanat = {
    "Matti" : {1, 2, 1, 4, 2},
    "Pekka" : {3, 4, 2, 3, 3},
    "Teppo" : {0, 5, 4, 5}}

arvosanat["Olga"] = 1, 4, 5
arvosanat["Matti"] = 2, 4, 2

for n in arvosanat:
    print(n + " arvosanat ovat", arvosanat[n])




#tuntitehtävä

hedelmat = {
    "Omena" : "1",
    "Appelsiini" : "2",
    "Päärynä" : "3",
    "Mango" : "4"
}

hedelma = input("Anna hedelmä, jonka hinnan haluat tietää (Omena, Appelsiini, Päärynä, Mango):")

print(f"{hedelma} maksaa {hedelmat[hedelma]} euroa")

#2 tuntitehtävä


hedelmat = {
    "Omena" : "1",
    "Appelsiini" : "2",
    "Päärynä" : "3",
    "Mango" : "4"
}

summa = 0

while True:
    hedelma = input("Anna hedelmä, jonka hinnat haluat lisätä summaan(tyhjä lopettaa)")
    if hedelma == "":
        print("Tilaus päättyy...")
    break

if hedelma in hedelmat:
    print(f"{hedelma} hinta on {hedelmat[hedelma]}")
    summa += {hedelmat[hedelma]}

else:
    print("Hedelmä ei ole listalla")

print("Yhteishinta on". summa, "euroa")

