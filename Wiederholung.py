zimmerpreis = float(input("Geben Sie den Zimmerpreis pro Person und Nacht ein: "))
aufenthaltsdauer = int(input("Geben Sie die Aufenthaltsdauer in Nächten ein: "))
alter_kind = int(input("Gebe bitte das alter des Kindes ein: "))
rabatt = 0 
kidnerpreis = 0

if alter_kind < 7 :
    rabatt = 100
else:
    rabatt = 70

kinderpreis = zimmerpreis*aufenthaltsdauer*(rabatt/100)

erwachsenepreis = 2*zimmerpreis*aufenthaltsdauer

gesamtpreis = erwachsenepreis+kinderpreis

print(f"Gesamtpreis für die Familie beträgt: {gesamtpreis:.2f} Euro")