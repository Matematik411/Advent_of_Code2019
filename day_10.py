def naloga1(vsebina_datoteke):
    tabela = vsebina_datoteke.split("\n")
    najvec = 0
    polje = None
    videni_max = {}
    koord_max = {}
    for y, line in enumerate(tabela):
        for x, a in enumerate(line):
            if a == "#":
                videni = set()
                koord = {}
                for i, vrstica in enumerate(tabela):
                    for j, k in enumerate(vrstica):
                        if k == "#":
                            if x == j and i == y:
                                pass
                            elif x == j and i > y:
                                if "infty" not in videni:
                                    videni.add(("infty", "othr"))
                                    koord[("infty", "othr")] = (j, i)
                            elif x == j and i < y:
                                if "-infty" not in videni:
                                    videni.add(("-infty", "othr"))
                                    koord[("-infty", "othr")] = (j, i)
                            elif y == i and j > x:
                                if "0" not in videni:
                                    videni.add(("0", "othr"))
                                    koord[("0", "othr")] = (j, i)
                            elif y == i and j < x:
                                if "-0" not in videni:
                                    videni.add(("-0", "othr"))
                                    koord[("-0", "othr")] = (j, i)
                            elif y < i:
                                if ((-i+y)/(j-x), "dol") not in videni:
                                    videni.add(((-i+y)/(j-x), "dol"))
                                    koord[((-i+y)/(j-x), "dol")] = (j, i)
                            else: # i > y
                                if ((-i+y)/(j-x), "gor") not in videni:
                                    videni.add(((-i+y)/(j-x), "gor"))
                                    koord[((-i+y)/(j-x), "gor")] = (j, i)
                if len(videni) > najvec:
                    najvec = len(videni)
                    polje = (x, y)
                    videni_max = videni
                    koord_max = koord

    return najvec, videni_max, koord_max

def naloga2(videni, koord):
    n = 230
    while n > 199:
        pravi = None
        vrednost = 0
        for ast in videni:
            if ast[1] == "gor":
                if ast[0] < vrednost:
                    pravi = ast
                    vrednost = ast[0]
        if vrednost >= 0:
            break
        else:
            videni.remove(pravi)
            n -= 1

    return str(koord[pravi][0]*100 + koord[pravi][1])


if __name__ == '__main__':
    with open('day_10.in', encoding='utf-8') as f:
        vsebina_datoteke = f.read()
    odgovor1, videni, koord = naloga1(vsebina_datoteke)
    with open('day_10_1.out', 'w', encoding='utf-8') as f:
        f.write(str(odgovor1))
    odgovor2 = naloga2(videni, koord)
    with open('day_10_2.out', 'w', encoding='utf-8') as f:
        f.write(odgovor2)