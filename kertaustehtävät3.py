#tehtävä 1

tiedot = {"John" : ["John", 30, "Engineer"],
"Emily" : ["Emily", 25, "Artist"],
"Anna" : ["Anna", 22, "Student"]}

print(tiedot["John"][0])
print(tiedot["John"][1])
print(tiedot["Emily"][2])

tiedot["Anna"][2] = "Teacher"
tiedot["James"] = ["James", 28, "Writer"]

tiedot["Sophia"] = ["Sophia", 35, "Doctor"]
del tiedot["Emily"]

print("Lopullinen sanakirja:")

for i in tiedot:
    print(tiedot[i])

#tehtävä 2

oppilaat = {
    "Maija": ["Maija", 4, "Matikka"],
    "Keijo": ["Keijo", 4, "Historia"],
    "Matti": ["Matti", 3, "Liikunta"],
    "Ronja": ["Ronja", 3, "Fysiikka"]
}

print(oppilaat["Maija"][1])
print(oppilaat["Keijo"][2])

oppilaat["Matti"][2] = "Englanti"
oppilaat["Kaija"] = ["Kaija", 3, "Kemia"]
del oppilaat["Ronja"]

print("Uusi päivitetty sanakirja: ")

for i in oppilaat:
    print(oppilaat[i])


#tehtävä 3

kirjasto = {
    "Tuntematon sotilas": ["Väinö Linna", 1954, "Sota"],
    "Seitsemän veljestä": ["Aleksis Kivi", 1870, "Klassikko"],
    "Sinuhe egyptiläinen": ["Mika Waltari", 1945, "Historiallinen"],
    "Risto Räppääjä": ["Sinikka Nopola", 1997, "Lastenkirja"]
}

print(kirjasto["Tuntematon sotilas"][0])
print(kirjasto["Seitsemän veljestä"][2])

kirjasto["Sinuhe egyptiläinen"][2] = "Seikkailu"
kirjasto["Kalevala"] = ["Elias Lönnrot", 1835, "Eepos"]
del kirjasto["Risto Räppääjä"]

print("Tässä päivitetty sanakirja: ")
for i in kirjasto:
    print(kirjasto[i])


