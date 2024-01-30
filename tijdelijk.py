mijn_prijzen = { 
    "aardbei" : "3",
    "vanille" : "4",
    "chocolade" : "5"
}

a =  mijn_prijzen["vanille"]
b = int(a)
aanbieding = b * 0.8

reclame_tekst = (f"vandaag in de aanbieding: vanille-ijs, 1 liter - slechts € {aanbieding}")
reclame_tekst3 =(f"vandaag in de aanbieding: vanille-ijs, 1 liter - slechts € {aanbieding}").upper()
reclame_tekst4 = reclame_tekst3.split()

for el in reclame_tekst4:
    if len(el)>4:
        print(el.upper())
    else:
        print(el.lower())