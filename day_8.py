def naloga1(vsebina_datoteke):
    dolzina = 25*6
    plasti = []
    nova = ""
    i = 0
    for a in vsebina_datoteke:
        nova +=a
        if i < dolzina - 1:
            i+=1
        else:
            plasti.append(nova)
            i = 0
            nova = ""

    nicle = (25*6, 0)    
    enice = 0
    dvojke = 0

    for i, pl in enumerate(plasti):
        x = pl.count("0")
        if x < nicle[0]:
            nicle = (x, i)

    enice = plasti[nicle[1]].count("1")
    dvojke = plasti[nicle[1]].count("2")

    return (enice*dvojke, plasti)

def naloga2(plasti):
    
    slika = ["2" for _ in range(25*6)]
    for plast in plasti:
        for x, a in enumerate(plast):
            if slika[x] == "2":
                slika[x] = str(a)
    niz = ""
    for i, im in enumerate(slika):
        if i % 25 == 0:
            niz += "\n"
        niz += im
    niz = niz.replace("0", " ").replace("1", "#")
    print(niz)

    return niz


if __name__ == '__main__':
    with open('day_8.in', encoding='utf-8') as f:
        vsebina_datoteke = f.read()
    odgovor1 = str(naloga1(vsebina_datoteke)[0])
    with open('day_8_1.out', 'w', encoding='utf-8') as f:
        f.write(odgovor1)
    odgovor2 = naloga2(naloga1(vsebina_datoteke)[1])
    with open('day_8_2.out', 'w', encoding='utf-8') as f:
        f.write(odgovor2)