#1

pituus = float(input("Kuinka pitkä kuha on? "))

if pituus < 37:
    print("Kuha on", 37-pituus, "cm liian lyhyt")
    print("Laske kuha takaisin järveen!")
else:
    print("Hieno kala!")


#2

hytti = input("Mikä on hyttiluokkasi?")

if hytti == "LUX":
    print("LUX on parvekkeellinen hytti yläkannella.")
elif hytti == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif hytti == "B":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif hytti == "C":
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka.")

#3

sukupuoli = input("Oletko mies vai nainen? ")
arvo = float(input("Mikä on hemoglobiiniarvosi? "))

if sukupuoli == "nainen" and arvo < 117:
    print("Hemoglobiiniarvosi on alhainen")
elif sukupuoli == "nainen" and arvo > 175:
    print("Hemoglobiiniarvosi on korkea.")
elif sukupuoli == "nainen" and 117 < arvo < 175:
    print("Hemoglobiiniarvosi on normaali.")
elif sukupuoli == "mies" and arvo < 134:
    print("Hemoglobiiniarvosi on alhainen.")
elif sukupuoli == "mies" and arvo > 195:
    print("Hemoglobiiniarvosi on korkea. ")
elif sukupuoli == "mies" and 134 < arvo < 195:
    print("Hemoglobiiniarvosi on normaali. ")
else:
    print("Virheellinen syöte")


#4

vuosi = int(input("Anna vuosi: "))

if (vuosi % 4 == 0 and vuosi % 100 != 0) or (vuosi % 400 == 0):
    print("Vuosi on karkausvuosi.")
else:
    print("Vuosi ei ole karkausvuosi.")

#5

luku =float(input("Anna luku: "))

if luku % 2 == 0 and luku % 3 == 0:
    print("Luku on parillinen ja jaollinen kolmella.")
elif luku % 2 == 0:
    print("Luku on parillinen.")
elif luku % 3 == 0:
    print("Luku on jaollinen kolmella.")
else:
    print("Luku ei ole jaollinen kolmella eikä parillinen.")

#6

oikea = "salainen"
yritykset = 3




while yritykset > 0:
    sana = input("Anna salasana: ")

    if sana == "salainen":
        print("Tervetuloa!")
        break
    else:
        yritykset -= 1
        print("Väärä salasana.")
if yritykset == 0:
    print("Pääsy evätty.")


#7

saldo = float(input("Mikä on pankkitilisi saldo? "))
nosto = float(input("Paljonko haluat nostaa? "))

if saldo <= nosto:
    print("Ei tarpeeksi rahaa.")
elif saldo >= nosto:
    print("Tilille jäi", saldo-nosto, "euroa")
else:
    print("Virheellinen syöte.")











