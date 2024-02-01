def mijn_functie_1(argument):
    tabel = {
        2: 4,
        4: 16,
        10: 100,
        12: 144
    }

    if argument in tabel:
        return(tabel[argument])
    else:
        return(None)

def mijn_functie_2(argument):
    tabel = {
        12.3: [15, 9, 36, 4],
        12.2: [14, 10, 24, 6],
        10.5: [15, 5, 50, 2],
        100.20: [120, 80, 2000, 5]
    }

    if argument in tabel:
        return(tabel[argument])
    else:
        return(None)