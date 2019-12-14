import re




def naloga1(vsebina_datoteke, prva):
    seznam = vsebina_datoteke.split("\n")
    iscem = r"(?P<x>\d+) (?P<ime>[A-Z]*)"
    novi = []
    imena = set()
    for enacba in seznam:
        en = []
        for hit in re.finditer(iscem, enacba):
            en.append((hit.groupdict()["ime"], int(hit.groupdict()["x"])))
            imena.update({hit.groupdict()["ime"]})
        novi.append(en)

    rabim = {"ORE" : 0}

    if prva:
        imam = {}
        for enacba in novi:
            if enacba[-1][0] == "FUEL":
                for ostalo in enacba[:-1]:
                    if ostalo[0] not in rabim:
                        rabim[ostalo[0]] = ostalo[1]
                    else:
                        rabim[ostalo[0]] += ostalo[1]

    
    else:
        imam = {}


    def potrebuje(stvar):
        imam_tega = imam.get(stvar, 0)

        if imam_tega < rabim[stvar]:

            rabim[stvar] -= imam_tega
            imam[stvar] = 0

            for enacba in novi:
                if enacba[-1][0] == stvar:
                    for ostalo in enacba[:-1]:
                        ime, vr = ostalo
                        a = vr - imam.get(ime, 0)
                        if a > 0:
                            imam[ime] = 0
                            if ime not in rabim:
                                rabim[ime] = a
                            else:
                                rabim[ime] += a
                        else:
                            imam[ime] -= vr


                    ostane = rabim[stvar] - enacba[-1][1] 
                    if ostane <= 0:
                        if ostane < 0:
                            if stvar not in imam:
                                imam[stvar] = -ostane
                            else:
                                imam[stvar] -= ostane
                        del rabim[stvar]
                        break
                    else:
                        rabim[stvar] = ostane
        else:
            imam[stvar] -= rabim[stvar]
            del rabim[stvar]


    if prva:
        while len(rabim) > 1:
            for k in imena:
                if k != "ORE" and k in rabim:
                    potrebuje(k)
        return str(rabim["ORE"])
    
    else:
        enote = 0

        while rabim["ORE"] < 1000000000000:
            rabim["FUEL"] = 1
            potrebuje("FUEL")
            
            while len(rabim) > 1:
                for k in imena:
                    if k != "ORE" and k in rabim:
                        potrebuje(k)

            enote += 1
            print(enote)
        return(str(enote - 1))
        


if __name__ == '__main__':
    
    with open('day_14.in', encoding='utf-8') as f:
        vsebina_datoteke = f.read()
    odgovor1 = naloga1(vsebina_datoteke, True)
    with open('day_14_1.out', 'w', encoding='utf-8') as f:
        f.write(odgovor1)
    # odgovor2 = naloga1(vsebina_datoteke, False)       SE NE KONČA V ZGLEDNEM ČASU xD
    # with open('day_14_2.out', 'w', encoding='utf-8') as f:
    #     f.write(odgovor2)