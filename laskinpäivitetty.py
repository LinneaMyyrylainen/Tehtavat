
def summa(a,b):
    return a + b
def erotus(a,b):
    return a - b
def tulo(a,b):
    return a * b
def jako(a,b):
    if b == 0:
        return "Ei voi jakaa nollalla"
    return a / b


while True:
    lasku = input("Valitse laskutoimitus (Yhteenlasku, Vähennyslasku, Jakolasku tai Kertolasku), Loppu lopettaa ohjelman.")

    if lasku == "Loppu":
        break
    if lasku == "Yhteenlasku" or lasku =="Vähennyslasku" or lasku =="Jakolasku" or lasku =="Kertolasku":
        luku1 = float(input("Anna ensimmäinen luku:"))
        luku2 = float(input("Anna toinen luku:"))

        if lasku == "Yhteenlasku":
            print("Lukujesi yhteenlaskun tulos on", summa(luku1, luku2))
        elif lasku == "Vähennyslasku":
            print("Lukujesi vähennyslaskun tulos on", erotus(luku1, luku2))
        elif lasku == "Kertolasku":
            print("Lukujesi kertolaskun tulos on", tulo(luku1, luku2))
        elif lasku == "Jakolasku":
            print("Lukujesi jakolaskun tulos on", jako(luku1, luku2))
    else:
        print("Virheellinen komento. Anna komento uudestaan.")


