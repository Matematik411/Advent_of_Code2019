def pot_zice(zica):
    slovar = {}
    x, y, d = 0, 0, 0
    smer = {"R" : [1, 0], "L" : [-1, 0], "U" : [0, 1], "D" : [0, -1]}
    for dogodek in zica:
        for _ in range(int(dogodek[1:])):
            usmerjenost = smer[dogodek[0]]
            x += usmerjenost[0]
            y += usmerjenost[1]
            d += 1
            if (x, y) not in slovar:
                slovar[(x, y)] = d
    return slovar

def naloga1(vsebina_datoteke):
    seznam = vsebina_datoteke.split("\n")
    pravi = []
    for string in seznam:
        pravi.append(string.split(","))
    
    prva_zica = pot_zice(pravi[0])
    druga_zica = pot_zice(pravi[1])
    
    skupna_polja = prva_zica.keys() & druga_zica.keys()

    Manh_razdalja = min([abs(a) + abs(b) for (a, b) in skupna_polja])
    pot_razdalja = min([prva_zica[i] + druga_zica[i] for i in skupna_polja])
    
    return (str(Manh_razdalja), str(pot_razdalja))


if __name__ == '__main__':
    with open('day_3.in', encoding='utf-8') as f:
        vsebina_datoteke = f.read()
    odgovor = naloga1(vsebina_datoteke)
    with open('day_3_1.out', 'w', encoding='utf-8') as f:
        f.write(odgovor[0])
    with open('day_3_2.out', 'w', encoding='utf-8') as f:
        f.write(odgovor[1])
    