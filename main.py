def waluta_dict_na_str(waluta_dict):

    waluta_str = ""

    if "galeon" in waluta_dict and waluta_dict["galeon"] != 0:
        waluta_str += f"{waluta_dict['galeon']} galeon "

    if "sykl" in waluta_dict and waluta_dict["sykl"] != 0:
        waluta_str += f"{waluta_dict['sykl']} sykl "

    if "knut" in waluta_dict and waluta_dict["knut"] != 0:
        waluta_str += f"{waluta_dict['knut']} knut "

    return waluta_str

# Przykład użycia:
bank = {
    "galeon": 1,
    "sykl": 2,
    "knut": 11
}
print(waluta_dict_na_str(bank))
