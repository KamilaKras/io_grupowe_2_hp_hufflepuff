import datetime
import random
import time
import csv

# zadanie 2
def wyslij_sowe(adresat, tresc_wiadomosci):
    print(f"Wysyłanie sowy z listem do {adresat} o treści: {tresc_wiadomosci}....")
    time.sleep(1)
    losowanie = random.choices((True, False), weights=[0.85, 0.15])[0]

    return losowanie


# wejscie1 = input("Podaj adresata: ")
# wejscie2 = input("Podaj treść listu: ")

# print(wyslij_sowe(wejscie1, wejscie2))

#zadanie 3
def licz_sume(skladniki):
    knuty_w_syklu = 21
    sykle_w_galeonie = 17

    # Sumowanie wartości monet
    suma_knutow = sum(skladniki.get('knut', []))
    suma_sykli = sum(skladniki.get('sykl', [])) + suma_knutow // knuty_w_syklu
    suma_galeonow = sum(skladniki.get('galeon', [])) + suma_sykli // sykle_w_galeonie

    # Obliczanie reszty knutów i sykli, które nie zmieściły się w wyższych nominałach
    knuty_reszta = suma_knutow % knuty_w_syklu
    sykle_reszta = suma_sykli % sykle_w_galeonie

    # Zwracanie słownika z przeliczonymi wartościami
    return {
        'galeon': suma_galeonow,
        'sykl': sykle_reszta,
        'knut': knuty_reszta
    }


# # Przykładowe dane wejściowe i uruchomienie
# try:
#     skladniki = {
#         'galeon': [1, 3, 5],
#         'sykl': [18, 20, 10],
#         'knut': [30, 40, 7]
#     }
#     wynik = licz_sume(skladniki)
#     print(f"Wynik po przeliczeniu: {wynik}")  # Powinno wypisać wynik przeliczenia
#
# except TypeError:
#     print("Błąd")

# zadanie 4
def wybierz_sowe_zwroc_koszt(p, o, t, s):
    g = 0
    syk = 0
    k = 0

    if bool(p) and str(s) == 'wyjec':
        k += 14
    elif bool(p) and str(s) == 'list gończy':
        syk += 1
        k += 7
    elif bool(p):
        k += 7
    elif str(s) == 'wyjec':
        k += 7
    elif str(s) == 'list gończy':
        syk += 1

    if str(o) == 'lokalna':
        if str(t) == 'list':
            k += 2
        elif str(t) == 'paczka':
            k += 7
    elif str(o) == 'krajowa':
        if str(t) == 'list':
            k += 12
        elif str(t) == 'paczka':
            syk += 1
            k += 2
    elif str(o) == 'dalekobieżna':
        if str(t) == 'list':
            k += 20
        elif str(t) == 'paczka':
            syk += 2
            k += 1

    while k > 21:
        k -= 21
        syk += 1
    while syk > 17:
        syk -= 17
        g += 1

    d = {'galeon': g,
         'sykl': syk,
         'knut': k}

    print(d)

    return d


# wybierz_sowe_zwroc_koszt(True, 'dalekobieżna', 'paczka', 'list gończy')

# zadanie 5
def waluta_dict_na_str(waluta_dict):
    waluta_str = ""

    if "galeon" in waluta_dict and waluta_dict["galeon"] != 0:
        waluta_str += f"{waluta_dict['galeon']} galeon "

    if "sykl" in waluta_dict and waluta_dict["sykl"] != 0:
        waluta_str += f"{waluta_dict['sykl']} sykl "

    if "knut" in waluta_dict and waluta_dict["knut"] != 0:
        waluta_str += f"{waluta_dict['knut']} knut "

    return waluta_str


# # Wprowadzanie danych przez użytkownika
# bank = {}
# bank["galeon"] = int(input("Podaj ilość galeonów: "))
# bank["sykl"] = int(input("Podaj ilość syklów: "))
# bank["knut"] = int(input("Podaj ilość knutów: "))
#
# print(waluta_dict_na_str(bank))



# zadanie 6
def waluta_str_na_dict(ciag_znakow):
    bilony = ciag_znakow.split()
    wynik = {}

    for i in range(0, len(bilony), 2):
        wartosc = int(bilony[i])
        rodzaj = bilony[i + 1]
        if rodzaj.startswith("g"):
            wynik["galeon"] = wartosc
        elif rodzaj.startswith("s"):
            wynik["sykl"] = wartosc
        elif rodzaj.startswith("k"):
            wynik["knut"] = wartosc
    if "galeon" not in wynik:
        wynik["galeon"] = 0
    if "sykl" not in wynik:
        wynik["sykl"] = 0
    if "knut" not in wynik:
        wynik["knut"] = 0

    wynik_str = "{\n" + f"'galeon': {wynik['galeon']},\n 'sykl': {wynik['sykl']},\n 'knut': {wynik['knut']}\n" + "}"
    return wynik_str

# ciag_znakow = str(input("Podaj bilony: "))
# print(waluta_str_na_dict(ciag_znakow))

# zadanie 7
def nadaj_sowe(a, t, potw1, odl1, typ1, sp1):
    potw2 = False

    if potw1.lower() == "tak":
        potw2 = True
    elif potw1.lower() == "nie":
        potw2 = False

    if odl1.lower() == "l":
        odl1 = "lokalna"
    elif odl1.lower() == "l":
        odl1 = "krajowa"
    elif odl1.lower() == "d":
        odl1 = "dalekobieżna"

    if typ1.lower() == "l":
        typ1 = "list"
    elif typ1.lower() == "p":
        typ1 = "paczka"

    if sp1.lower() == "z":
        sp1 = "zwykła"
    elif sp1.lower() == "w":
        sp1 = "wyjec"
    elif sp1.lower() == "l":
        sp1 = "list gończy"

    koszt_przesylki = waluta_dict_na_str(wybierz_sowe_zwroc_koszt(p=potw2, o=str(odl1), t=str(typ1), s=str(sp1)))

    if potw2:
        with open('poczta_nadania_lista.csv',mode='a',newline='') as plik:
            csv_writer = csv.writer(plik)
            csv_writer.writerow([a, t, str(koszt_przesylki), "Tak"])
    elif not potw2:
        with open('poczta_nadania_lista.csv',mode='a',newline='') as plik:
            csv_writer = csv.writer(plik)
            csv_writer.writerow([a, t, str(koszt_przesylki), "Nie"])


adresat = str(input("Podaj adresata: "))
tresc = str(input("Podaj treść wiadomości: "))
potw = input("Czy chcesz potwierdzenie odbioru? Tak/Nie: ")
odl = str(input("Podaj odległość. L - lokalna, K - krajowa, D - dalekobieżna: "))
typ = str(input("Podaj typ przesyłki. L - list, P - paczka: "))
sp = str(input("Zwykła czy specjalna? Z - zwykła, W - wyjec, L - list gończy: "))

nadaj_sowe(adresat, tresc, potw, odl, typ, sp)


# zadanie 8

def poczta_wyslij_sowy(sciezka_do_pliku_csv):
    dzisiaj = datetime.datetime.now().strftime("%d_%m_%Y")
    output_file = f"output_sowy_z_poczty_{dzisiaj}.csv"
    
    try:
        with open(sciezka_do_pliku_csv, mode='r', encoding='utf-8') as csvfile, \
            open(output_file, mode='w', encoding='utf-8', newline='') as output_csvfile:
            
            fieldnames = ['adresat', 'tresc wiadomosci', 'koszt przesylki', 'potwierdzenie odbioru', 'rzeczywisty koszt']
            
            writer = csv.DictWriter(output_csvfile, fieldnames=fieldnames)
            writer.writeheader()

            
            reader = csv.reader(csvfile)
            for values in reader:
                
                row_data = dict(zip(fieldnames, values))
                
                adresat = row_data.get('adresat', '').strip()
                tresc_wiadomosci = row_data.get('tresc wiadomosci', '').strip()
                koszt_przesylki = row_data.get('koszt przesylki', '').strip()
                potwierdzenie_odbioru = row_data.get('potwierdzenie odbioru', '').strip()
                
                sowa_doleciala = wyslij_sowe(adresat, tresc_wiadomosci)
                print(f"Wartość zwrócona przez funkcję wyslij_sowe: {sowa_doleciala}")
                
                if sowa_doleciala:
                    rzeczywisty_koszt = koszt_przesylki
                else:
                    if potwierdzenie_odbioru == 'Tak':
                        rzeczywisty_koszt = 0.0
                    else:
                        rzeczywisty_koszt = koszt_przesylki
                
                writer.writerow({
                    'adresat': adresat,
                    'tresc wiadomosci': tresc_wiadomosci,
                    'koszt przesylki': koszt_przesylki,
                    'potwierdzenie odbioru': potwierdzenie_odbioru.upper(),
                    'rzeczywisty koszt': rzeczywisty_koszt
                })
        
        print(f"Wyniki zapisano w pliku: {output_file}")
    except Exception as e:
        print(f"Wystąpił błąd podczas przetwarzania danych: {e}")

# Przykładowe wywołanie funkcji
poczta_wyslij_sowy('poczta_nadania_lista.csv')

