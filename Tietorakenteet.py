#lista

my_list = [4, 15, 3, 0, 1]
tyhja_lista = []

#tietorakenteissa voi olla monta arvoa

#monikko

#monikkoa ei voi muuttaa enää jälkeenpäin
#alkaa nollasta

my_tuple = ("Kevät", "Kesä", "Syksy", "Talvi")
#ei voi luoda tyhjää koska sitä ei voi muuttaa

viikonpaivat = ("Ma", "Ti", "Ke", "To", "Pe", "La", "Su")

paiva = int(input("Anna järjestysnumero, jonka päivän haluat tarkistaa (1-7): "))

viikonpaiva = viikonpaivat[paiva-1]

print("Numeroa vastaava päivä on", viikonpaiva)


#joukko

pelit = {"Kimble", "Uno", "Afrikantähti"}
print(pelit)

my_set = {"Audi", "Mese", "BMW"}
tyhja_joukko = set{}

#voi lisätä ja poistaa


#sanakirja

arvosanat = {
    "Matti" : {1, 2, 1, 4, 2},
    "Pekka" : {3, 4, 2, 3, 3},
    "Teppo" : {0, 5, 4, 5}}
