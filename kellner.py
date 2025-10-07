#START
def essen_fertig_callback():
    print("Kellner holt das Essen ab.")
    print("Kellner bringt das Essen zum Kunden.")
    print("Kunde erhält das Essen.")

def küche_bereitet_essen_vor(callback):
    print("Küche bereitet das Essen zu...")
    print("Essen ist fertig!")
    callback()  # → Callback wird ausgelöst

# Hauptprogramm
print("Kunde bestellt ein Gericht.")
print("Kellner bringt die Bestellung in die Küche.")
küche_bereitet_essen_vor(callback=essen_fertig_callback)
print("Vorgang abgeschlossen.")
#END