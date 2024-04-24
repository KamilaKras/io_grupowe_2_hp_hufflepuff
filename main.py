def waluta_dict_na_str(waluta_dict):

    waluta_str = ""

    if "galeon" in waluta_dict and waluta_dict["galeon"] != 0:
        waluta_str += f"{waluta_dict['galeon']} galeon "

    if "sykl" in waluta_dict and waluta_dict["sykl"] != 0:
        waluta_str += f"{waluta_dict['sykl']} sykl "

    if "knut" in waluta_dict and waluta_dict["knut"] != 0:
        waluta_str += f"{waluta_dict['knut']} knut "

    return waluta_str

# Wprowadzanie danych przez użytkownika
bank = {}
bank["galeon"] = int(input("Podaj ilość galeonów: "))
bank["sykl"] = int(input("Podaj ilość syklów: "))
bank["knut"] = int(input("Podaj ilość knutów: "))

print(waluta_dict_na_str(bank))



        