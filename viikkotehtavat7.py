#tehtävä 1

kuukaudet = ("Talvi", "Talvi", "Kevät", "Kevät", "Kevät", "Kesä", "Kesä", "Kesä", "Syksy", "Syksy", "Syksy", "Talvi")

kuukausi = int(input("Anna kuukauden numero, jonka vuodenajan haluat tietää:"))

if kuukausi >= 0 and kuukausi <= 12:
    print("Kuukautesi numeroa vastaava vuodenaika on", kuukaudet[kuukausi-1])
else:
    print("Antamasi numero ei vastaa kuukautta...")

#tehtävä 2

nimet = set()

while True:
    nimi = input("Anna nimi, jonka haluat lisätä listaan (tyhjä lopettaa):")

    if nimi == "":
        break
    elif nimi in nimet:
        print("Aiemmin syötetty nimi.")
    else:
        print("Uusi nimi.")
        nimet.add(nimi)

for n in nimet:
    print(n)

#tehtävä 3

tiedot = {
    "EFHK" : "Helsinki",
    "ESSA" : "Tukholma",
    "LEMG" : "Malga",
    "LEMD" : "Madrid",
    "LIRF" : "Rooma",
    "VTBS" : "Bangkok"
}

while True:
    kysymys = input("Haluatko syöttää uuden lentoaseman(1), hakea jo syötetyn lentoaseman tiedot(2) vai lopettaa(3)?")

    if kysymys == "3":
        break
    elif kysymys == "1":
        ICAO = input("Anna lentoaseman ICAO-koodi: ")
        nimi = input("Anna lentoaseman nimi: ")
        tiedot[ICAO] = nimi
    elif kysymys == "2":
        ICAO = input("Anna lentoaseman ICAO-koodi: ")
        print("ICAO-koodia vastaava kaupunki on", tiedot.get(ICAO))
    else:
        print("Virheellinen syöte...")

