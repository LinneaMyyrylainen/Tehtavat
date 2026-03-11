#lista

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



