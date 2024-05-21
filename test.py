from main import wyslijsowe
from unittest.mock import patch
from main import waluta_str_na_dict

# testy - zadanie1

def test_wyslij_sowe():
    liczba_sukcesow = 0
    liczba_prob = 10000

    with patch('main.time.sleep', return_value=None):
        for _ in range(liczba_prob):
            if wyslijsowe("adrest", "tresc_listu"):
                liczba_sukcesow += 1

    wspolczynnik_sukcesow = liczba_sukcesow / liczba_prob

    # sprawdzanie, czy sukces pojawia się w okolicach 85%
    # można sprawdzić podstawiając inny zakres, że wychodzą wtedy błędy
    assert 0.80 <= wspolczynnik_sukcesow <= 0.90


test_wyslij_sowe()


def test_waluta_str_na_dict():
    #poprawne dane
    wynik = waluta_str_na_dict("5 galeonów 10 sykli 15 knutów")
    assert wynik == "{\n'galeon': 5,\n 'sykl': 10,\n 'knut': 15\n}"
    #brak sykli
    wynik = waluta_str_na_dict("5 galeonów 15 knutów")
    assert wynik == "{\n'galeon': 5,\n 'sykl': 0,\n 'knut': 15\n}"
    #nieprawidlowe waluty
    wynik = waluta_str_na_dict("5 pln 10 euro 15 usd")
    assert wynik == "{\n'galeon': 0,\n 'sykl': 0,\n 'knut': 0\n}"

test_waluta_str_na_dict()