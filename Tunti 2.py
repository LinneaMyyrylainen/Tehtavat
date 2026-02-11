from operator import truediv

raha=float(input("Kuinka paljon sinulla on rahaa?"))
if raha >=5:
    print("Voit ostaa kahvin.")

else:
    puuttuva = 5 - raha
    print("Sorry, sinulta puuttuu", puuttuva)

print("Kiitos hei!")



a = True
b = False

if a and b:
    print("Molemmat on totta.")

if a or b:
    print("Toinen ehto oli totta.")

if not a or b:
    print("Kumpikaan ei ole totta:")


numero = int(input("Anna kokonaisluku: "))

if numero > 0:
    print("Luku on positiivinen.")
elif numero < 0:
    print("Luku on negatiivinen.")
else:
    print("Numero oli 0.")


ika = int(input("Kuinka vanha olet?"))

if ika >=65:
    print("Olet eläkeiässä:")
elif ika >= 18:
    print("Olet työikäinen.")
elif ika >= 7:
    print("Olet kouluiässä.")
else:
    print("Olet pieni lapsi.")


numero = int(input("Anna luku: "))

if numero>0:
    if numero % 2 == 0:
        print("Numero on parillinen.")
    else:
        print("Numero on pariton.")

else:
    print("Numero jonka annoit on negatiivinen:")

print("Jatketaan...")

