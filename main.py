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