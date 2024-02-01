from algemene_functies import mijn_functie_2

def aanbieding_1(smaak, prijs, korting):
    korting = prijs * korting
    print(f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {prijs - korting} euro.")

aanbieding_1("aardbei", 4, 0.1)

def inkomsten_totaal(inkomsten, btw):
    totaal_inkomsten = sum(inkomsten)
    kosten_btw = totaal_inkomsten * btw
    print(f"Het totaal van alle inkomsten van deze week is {totaal_inkomsten} euro, waarover {kosten_btw} euro btw betaald dient te worden.")
inkomsten_totaal([220, 430, 125, 160, 205, 90, 345], 0.09)

def laag_en_hoog(mijn_lijst):
    laagste = min(mijn_lijst)
    hoogste = max(mijn_lijst)
    print(f"{[laagste, hoogste]}")
laag_en_hoog([220, 430, 125, 160, 205, 90, 345])

def gemiddelde(mijn_lijst):
    totaal = sum(mijn_lijst)
    gemiddeld = totaal / 7
    print(f"De gemiddelde inkomsten deze week zijn {gemiddeld} euro.")
gemiddelde([220, 430, 125, 160, 205, 90, 345])

def meervoudig(invoer_lijst):
    laag_en_hoog(invoer_lijst)
meervoudig([10,5,3,2,1,2,9])

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer