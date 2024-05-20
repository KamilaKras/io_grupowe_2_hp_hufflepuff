from main import waluta_str_na_dict

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