zimmerpreis = float(input("Geben sie bitte den Zimmerpreis für heute ein: "))
aufenthaltsdauer = float(input("Geben sie bitte die Dauer ein: "))
anzahl_kinder = int(input("Wie viele Kinder hat die Familie eingecheckt: "))

kidnerpreis = 0.0
zaehler=0

while zaehler < anzahl_kinder: # zähle ich gleich runter und zaehler 0
    alter_kind = int(input(f"Gebe jetzt an wie alt das Kind ist: {zaehler+1}"))

    if alter_kind <= 6:
        rabatt = 100
    else:
        rabatt = 50

    kinderpreis = kinderpreis+zimmerpreis*aufenthaltsdauer*(1-rabatt/100)
    zaehler+=1

erwachsenepreis = 2*zimmerpreis*aufenthaltsdauer
gesamtpreis = erwachsenepreis+kinderpreis

print("Angebot für diese wunderbare Familie")
print(f"\n Zimmerpreis Nacht und Person: {zimmerpreis:.2f} € und Aufenhaltsdauer {aufenthaltsdauer} in Nächte und Preis für die komplette Familie: {gesamtpreis:.2f} €")