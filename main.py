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