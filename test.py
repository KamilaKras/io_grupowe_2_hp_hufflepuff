import csv
import os
from main import nadaj_sowe, poczta_wyslij_sowy, waluta_dict_na_str, wybierz_sowe_zwroc_koszt, wyslij_sowe
from unittest.mock import patch
from main import waluta_str_na_dict
from main import licz_sume
import unittest

class TestMainMethods(unittest.TestCase):

    def setUp(self):
        # Tworzenie tymczasowego pliku przed każdym testem
        self.test_file = 'test_data.csv'
        with open(self.test_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['adresat', 'tresc wiadomosci', 'koszt przesylki', 'potwierdzenie odbioru'])

    def tearDown(self):
        # Usuwanie pliku po każdym teście
        os.remove(self.test_file)
        
    def test_wyslij_sowe(self):
        liczba_sukcesow = 0
        liczba_prob = 10000

        with patch('main.time.sleep', return_value=None):
            for _ in range(liczba_prob):
                if wyslij_sowe("adrest", "tresc_listu"):
                    liczba_sukcesow += 1

        wspolczynnik_sukcesow = liczba_sukcesow / liczba_prob

        # sprawdzanie, czy sukces pojawia się w okolicach 85%
        # można sprawdzić podstawiając inny zakres, że wychodzą wtedy błędy
        self.assertTrue(0.83 <= wspolczynnik_sukcesow <= 0.87)

    def test_waluta_str_na_dict(self):
        #poprawne dane
        wynik = waluta_str_na_dict("5 galeonów 10 sykli 15 knutów")
        expected = "{\n'galeon': 5,\n 'sykl': 10,\n 'knut': 15\n}"
        self.assertEqual(wynik, expected)
        #brak sykli
        wynik = waluta_str_na_dict("5 galeonów 15 knutów")
        expected = "{\n'galeon': 5,\n 'sykl': 0,\n 'knut': 15\n}"
        self.assertEqual(wynik, expected)
        #nieprawidlowe waluty
        wynik = waluta_str_na_dict("5 pln 10 euro 15 usd")
        expected = "{\n'galeon': 0,\n 'sykl': 0,\n 'knut': 0\n}"
        self.assertEqual(wynik, expected)

    def test_licz_sume(self):
        # Test pustych składników
        self.assertEqual(licz_sume({}), {'galeon': 0, 'sykl': 0, 'knut': 0})

        # Test braku gdy dwie waluty rowne zero
        skladniki = {'sykl': [10]}
        self.assertEqual(licz_sume(skladniki), {'galeon': 0, 'sykl': 10, 'knut': 0})

        # Test sumy bez przewalutowania
        skladniki = {'knut': [5, 15], 'sykl': [5], 'galeon': [1]}
        self.assertEqual(licz_sume(skladniki), {'galeon': 1, 'sykl': 5, 'knut': 20})
        
        # Test przewalutowania do wyższych
        self.assertEqual(licz_sume({'knut': [42], 'sykl': [34]}), {'galeon': 2, 'sykl': 2, 'knut': 0})

        # Test mieszanych
        self.assertEqual(licz_sume({'knut': [8, 13, 5], 'sykl': [16, 2], 'galeon': [2]}), {'galeon': 3, 'sykl': 2, 'knut': 5})

    def test_wybierz_sowe_zwroc_koszt(self):
        self.assertEqual(wybierz_sowe_zwroc_koszt(False, 'lokalna', 'list', 'zwykla'), {'galeon': 0, 'sykl': 0, 'knut': 2})
        self.assertEqual(wybierz_sowe_zwroc_koszt(True, 'krajowa', 'list', 'list gończy'), {'galeon': 0, 'sykl': 1, 'knut': 19})

    def test_waluta_dict_na_str(self):
        self.assertEqual(waluta_dict_na_str({'galeon': 2, 'sykl': 3, 'knut': 15}), '2 galeon 3 sykl 15 knut ')
        self.assertEqual(waluta_dict_na_str({'galeon': 0, 'sykl': 5, 'knut': 7}), '5 sykl 7 knut ')
        self.assertEqual(waluta_dict_na_str({'galeon': 0, 'sykl': 0, 'knut': 0}), '')
        self.assertEqual(waluta_dict_na_str({'galeon': 1, 'sykl': 1, 'knut': 0}), '1 galeon 1 sykl ')

    

if __name__ == '__main__':
    unittest.main()