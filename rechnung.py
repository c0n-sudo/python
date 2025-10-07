#START
def quittung_callback():
    print("Zahlung erfolgreich.")
    print("Quittung wird gedruckt...")

def kunde_zahlt(callback):
    print("Kunde zahlt die Rechnung...")
    callback()  # → Callback wird ausgelöst

# Hauptprogramm
print("Kunde bittet um die Rechnung.")
print("Kellner bringt die Rechnung.")
kunde_zahlt(callback=quittung_callback)
print("Rechnungsvorgang abgeschlossen.")
#END