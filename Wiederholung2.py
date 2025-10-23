import random

print("Geben Sie eine Zahl zwischen 1 bis 5 ein: ")
input_value=input()

if input_value.isdigit():
    input_value=int(input_value)
    zufallszahl=random.randint(1,5)
    if input_value==zufallszahl:
        print("Herzlichen Glückwunsch du hast gewonnen!")
    else:
        print(f"Schade sie haben verloren, die korrekte Zahl war:{zufallszahl}")
else:
    print("Ungelütige Eingabe, bitte eine Zahl eingeben")


print("Danke fürs mitspielen!")