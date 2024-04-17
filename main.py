def waluty_na_str(waluty):
    result=""
    if 'galeony' in waluty and waluty['galeony']!=0:
        result += f"{waluty['galeony']} galeony"
    if 'sykle' in waluty and waluty['sykle']!=0:
        result += f"{waluty['sykle']} sykle"
    if 'knuty' in waluty and waluty['knuty']!=0:
        result += f"{waluty['knuty']} knuty"

    #PRZELICZANIE
    if knuty >= 21:
        sykle = waluty.get('sykle',0)+waluty.get('knuty',0) * 21
    if sykle >= 17:
        galeony = waluty.get('galeony',0)+waluty.get('sykle',0) * 17
    
return result.strip()