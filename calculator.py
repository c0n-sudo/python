# Funktionen für die Grundrechenarten
def addiere(x, y):
    return x + y

def subtrahiere(x, y):
    return x - y

def multipliziere(x, y):
    return x * y

def dividiere(x, y):
    if y == 0:
        return "Fehler: Division durch 0 ist nicht erlaubt!"
    return x / y

# Menü anzeigen
print("Willkommen zum einfachen Taschenrechner!")
print("Was möchtest du tun?")
print("1. Addieren")
print("2. Subtrahieren")
print("3. Multiplizieren")
print("4. Dividieren")

# Auswahl abfragen
wahl = input("Bitte gib 1, 2, 3 oder 4 ein: ")

# Zahlen abfragen (hier KEINE Fehlerprüfung!)
zahl1 = float(input("Gib die erste Zahl ein: "))
zahl2 = float(input("Gib die zweite Zahl ein: "))

# Rechenoperation je nach Auswahl ausführen
if wahl == '1':
    print("Ergebnis:", addiere(zahl1, zahl2))
elif wahl == '2':
    print("Ergebnis:", subtrahiere(zahl1, zahl2))
elif wahl == '3':
    print("Ergebnis:", multipliziere(zahl1, zahl2))
elif wahl == '4':
    print("Ergebnis:", dividiere(zahl1, zahl2))
else:
    print("Ungültige Auswahl. Bitte nur 1, 2, 3 oder 4 eingeben.")
