def tervehdys(teksti, kerrat):
    for i in range(kerrat):
        print(teksti)
    return

#Pääohjelma
print("Tästä ohjelma alkaa:")
tervehdys("Hello",3)
tervehdys("Päivää", 5)
tervehdys("Hyvää iltaa", 2)
print("Tähän ohjelma päättyy.")


def vaihda_nimi():
    kaupunki = "Vantaa"
    print("Funktion päättyessä kaupunki on", kaupunki)
    return

kaupunki = "Helsinki"
print("Ennen funktiokutsua kaupunkion", kaupunki)
vaihda_nimi()
print("Funktiokutsun jälkeen kaupunki on", kaupunki)