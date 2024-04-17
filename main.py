import random
import time


def wyslijsowe(adresat, tresc_listu):
    print(f"Wysyłanie sowy z listem do {adresat} o treści: {tresc_listu}....")
    time.sleep(1)
    losowanie = random.choices((True, False), weights=[0.85, 0.15])[0]

    return losowanie


wejscie1 = input("Podaj adresata: ")
wejscie2 = input("Podaj treść listu: ")

print(wyslijsowe(wejscie1, wejscie2))
