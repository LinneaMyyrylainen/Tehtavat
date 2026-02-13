#1 tehtävä
pituus=float(input("Kuinka pitkä kuha on?"))
if pituus<37:
    print("Laske kuha takaisin järveen.")
    print("Kuhan pitää olla ",37 - pituus, " cm pidempi!")

#2 tehtävä

hyttiluokka=input("Mikä on hyttiluokkasi?")
if hyttiluokka=="A":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif hyttiluokka=="B":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif hyttiluokka=="C":
    print("C on ikkunaton hytti autokannen alapuolella.")
elif hyttiluokka=="LUX":
    print("LUX on parvekkeellinen hytti yläkannella.")
else:
    print("Virheellinen hyttiluokka.")

#tehtävä 3

sukupuoli = input("Mikä on sinun biologinen sukupuoli?")
arvo = float(input("Mikä on hemoglobiiniarvosi?"))


if sukupuoli== "Nainen" and arvo < 117:
    print("Hemoglobiiniarvosi on alhainen")
elif sukupuoli== "Nainen" and arvo > 175:
    print("Hemoglobiiniarvosi on korkea")
elif sukupuoli== "Nainen" and 117 <= arvo < 175:
    print("Hemoglobiiniarvosi on normaali")
elif sukupuoli== "Mies" and arvo< 134:
    print("Hemoglobiiniarvosi on alhainen")
elif sukupuoli== "Mies" and arvo> 195:
    print("Hemoglobiiniarvosi on korkea")
elif sukupuoli== "Mies" and 134 <= arvo < 195:
    print("Hemoglobiiniarvosi on normaali")


#Tehtävä 4

luku = int(input("Anna vuosiluku."))

if luku % 400 == 0:
    print("Antamasi vuosiluku on karkausvuosi.")
elif luku % 100 == 0:
    print("Antamasi vuosiluku ei ole karkausvuosi.")
elif luku % 4 == 0:
    print("Antamasi vuosiluku on karkausvuosi.")
else:
    print("Antamasi vuosiluku ei ole karkausvuosi.")
