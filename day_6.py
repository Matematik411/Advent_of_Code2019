slovar = {}
def dodaj(item):
    if item[0] not in slovar:
        slovar[item[0]] = []
    slovar[item[0]].append(item[1])

def prestej(primer):
    velikost = 0
    for okoli in slovar.get(primer, []):
        velikost += prestej(okoli)
        velikost += 1
    return velikost

def naloga1(vsebina_datoteke):
    seznam = vsebina_datoteke.split()
    for orbit in seznam:
        prvi, drugi = orbit.split(")")
        dodaj((prvi, drugi))
    skupno = 0
    for planet in slovar:
        skupno += prestej(planet)
    return str(skupno)

def pot_nazaj(planet):
    pot = [planet]
    for key, value in slovar.items():
        if planet in value:
            pot = pot + pot_nazaj(key)
    return pot
        

def naloga2(vsebina_datoteke):
    pot_YOU = pot_nazaj("YOU")
    pot_SAN = pot_nazaj("SAN")

    dolzina = 0
    for i, orbit in enumerate(pot_YOU):
        if orbit in pot_SAN:
            dolzina += i - 1
            dolzina += pot_SAN.index(orbit) - 1
            break

    return str(dolzina)


if __name__ == '__main__':
    with open('day_6.in', encoding='utf-8') as f:
        vsebina_datoteke = f.read()
    odgovor1 = naloga1(vsebina_datoteke)
    with open('day_6_1.out', 'w', encoding='utf-8') as f:
        f.write(odgovor1)
    odgovor2 = naloga2(vsebina_datoteke)
    with open('day_6_2.out', 'w', encoding='utf-8') as f:
        f.write(odgovor2)