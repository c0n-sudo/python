import locale
locale.setlocale(locale.LC_ALL, 'de_DE.UTF-8')

strompreis = 0.40 # Euro pro kWh

verbrauch_tv = 3*1*3*365 # 3 kW, 1 Stunde pro Tag, 3 Geräte, 365 Tage
verbrauch_herd = 4*2*2*52 # 4 kW, 2 Stunden pro Tag, 2 Geräte, 52 Wochen
verbrauch_router = 2*4*365 # 2 kW, 4 Stunden pro Tag, 365 Tage
verbrauch_heizung = 8*20*170 # 8 kW, 20 Stunden pro Tag, 170 Tage

gesamtverbrauch = verbrauch_tv + verbrauch_herd + verbrauch_router + verbrauch_heizung
kosten = gesamtverbrauch * strompreis 

print("Kosten für den Stromverbrauch :", locale.currency(kosten, grouping=True))

