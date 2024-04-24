import random
import time

def wybierz_sowe_zwroc_koszt(p, o, t, s):
    g = 0
    syk = 0
    k = 0

    if p and s == 'wyjec':
        k += 14
    elif p and s == 'list gończy':
        syk += 1
        k += 7
    elif p:
        k += 7
    elif s == 'wyjec':
        k += 7
    elif s == 'list gończy':
        syk += 1

    if o == 'lokalna':
        if t == 'list':
            k += 2
        elif t == 'paczka':
            k += 7
    elif o == 'krajowa':
        if t == 'list':
            k += 12
        elif t == 'paczka':
            syk += 1
            k += 2
    elif o == 'dalekobieżna':
        if t == 'list':
            k += 20
        elif t == 'paczka':
            syk += 2
            k += 1

    while k > 21:
        k -= 21
        syk += 1
    while syk > 17:
        syk -= 17
        g += 1

    d = {'galeony': g,
         'sykle': syk,
         'knuty': k}

    print(d)


wybierz_sowe_zwroc_koszt(True, 'dalekobieżna', 'paczka', 'list gończy')



def wyslijsowe(adresat, tresc_listu):
    print(f"Wysyłanie sowy z listem do {adresat} o treści: {tresc_listu}....")
    time.sleep(1)
    losowanie = random.choices((True, False), weights=[0.85, 0.15])[0]

    return losowanie


wejscie1 = input("Podaj adresata: ")
wejscie2 = input("Podaj treść listu: ")

print(wyslijsowe(wejscie1, wejscie2))
def licz_sume(skladniki):
    knuty_w_syklu = 21
    sykle_w_galeonie = 17

    # Sumowanie wartości monet
    suma_knutow = sum(skladniki.get('knut', []))
    suma_sykli = sum(skladniki.get('sykl', [])) + suma_knutow // knuty_w_syklu
    suma_geleonow = sum(skladniki.get('geleon', [])) + suma_sykli // sykle_w_galeonie

    # Obliczanie reszty knutów i sykli, które nie zmieściły się w wyższych nominałach
    knuty_reszta = suma_knutow % knuty_w_syklu
    sykle_reszta = suma_sykli % sykle_w_galeonie

    # Zwracanie słownika z przeliczonymi wartościami
    return {
        'galeon': suma_geleonow,
        'sykl': sykle_reszta,
        'knut': knuty_reszta
    }

# Przykładowe dane wejściowe i uruchomienie
try:
    skladniki = {
        'galeon': [1, 3, 5],
        'sykl': [18, 20, 10],
        'knut': [30, 40, 7]
    }
    wynik = licz_sume(skladniki)
    print(f"Wynik po przeliczeniu: {wynik}")  # Powinno wypisać wynik przeliczenia

except TypeError:
    print("Błąd")
