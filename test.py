from main import wyslijsowe
from unittest.mock import patch
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
