import re
def naloga1(lune):
    st = 1000
    hitrosti = []
    # zacetno_stanje = [
    #     [lune[0][k] for k in lune[0]],
    #     [lune[1][k] for k in lune[2]],
    #     [lune[2][k] for k in lune[2]]
    # ]

    while st > 0:
        for i, moon in enumerate(lune):
            if len(hitrosti) < 4:
                tren = {'x':0, 'y':0, 'z':0}
            else:
                tren = hitrosti[i]
            for j, druga in enumerate(lune):
                if i != j:
                    for smer in tren:
                        if moon[smer] > druga[smer]:
                            tren[smer] -= 1
                        if moon[smer] < druga[smer]:
                            tren[smer] += 1
            if len(hitrosti) < 4:
                hitrosti.append(tren)
        for i, moon in enumerate(lune):
            for smer, sprememba in hitrosti[i].items():
                moon[smer] += sprememba
        # print(lune)
        # print(hitrosti)
        st -= 1
        # prvi = [lune[0][k] for k in lune[0]]
        # if prvi == zacetno_stanje[0]:
        #     if [lune[1][k] for k in lune[1]] == zacetno_stanje[1]:
        #         if [lune[2][k] for k in lune[2]] == zacetno_stanje[2]:
        #             if [hitrosti[0][k] for k in hitrosti[0]] == [0,0,0] == [hitrosti[1][k] for k in hitrosti[1]] == [hitrosti[2][k] for k in hitrosti[2]]:
        #                 return str(st)

        # for moon in lune:
        #     for v in moon.values():
        #         test.append(v)     
        # if test in polozaji:
        #     res_enako = True
        #     for hitr in hitrosti:
        #         for v in hitr.values():
        #             if v != 0:
        #                 res_enako = False
        #     if res_enako:
        #         return str(st)
        #     else:
        #         polozaji.append(test)
        # else:
        #     polozaji.append(test)
        # print(polozaji)
        # print(lune)   
    energija = 0
    for i, moon in enumerate(lune):
        pot = 0
        for v in moon.values():
            pot += abs(v)
        kin = 0
        for v in hitrosti[i].values():
            kin += abs(v)
        energija += pot * kin

            
    return str(energija)

def lcm(a, b):
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a
    return (a * b) // gcd(a, b)


def naloga2(lune):
    smeri = ["x", "y", "z"]
    skupno = 1
    for s in smeri:
        st = 0
        hitrosti = [0, 0, 0, 0]
        zacetno_stanje = [lune[0][s], lune[1][s], lune[2][s], lune[3][s]]
        stanje = [lune[0][s], lune[1][s], lune[2][s], lune[3][s]]
        while True:
            for i, moon in enumerate(stanje):
                for j, druga in enumerate(stanje):
                    if i != j:
                        if moon > druga:
                            hitrosti[i] -= 1
                        if moon < druga:
                            hitrosti[i] += 1
            for i in range(4):
                stanje[i] += hitrosti[i]
            st += 1
            if stanje == zacetno_stanje and hitrosti == [0, 0, 0, 0]:
                skupno = lcm(skupno, st)
                break
    


    return str(skupno)


if __name__ == '__main__':
    with open('day_12.in', encoding='utf-8') as f:
        data = []
        for vrst in f:
            iskalni = r'<x=(?P<x>(-)?\d*), y=(?P<y>(-)?\d*), z=(?P<z>(-)?\d*)>.*'
            for hit in re.finditer(iskalni, vrst):
                slo = hit.groupdict()
                for k, v in slo.items():
                    slo[k] = int(v)
                data.append(slo)
    print(data)

    # odgovor1 = naloga1(data)
    # with open('day_12_1.out', 'w', encoding='utf-8') as f:
    #     f.write(odgovor1)
    odgovor2 = naloga2(data)
    with open('day_12_2.out', 'w', encoding='utf-8') as f:
        f.write(odgovor2)