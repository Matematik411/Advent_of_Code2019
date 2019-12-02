def naloga1(vsebina_datoteke):
    seznam = list(map(int, vsebina_datoteke.split(',')))
    seznam[1] = 12
    seznam[2] = 2
    i = 0
    while seznam[i] != 99:
        if seznam[i] == 1:
            a = seznam[seznam[i+1]]
            b = seznam[seznam[i+2]]
            seznam[seznam[i+3]] = a + b
            i += 4
        elif seznam[i] == 2:
            a = seznam[seznam[i+1]]
            b = seznam[seznam[i+2]]
            seznam[seznam[i+3]] = a * b
            i += 4
    return str(seznam[0])

def splosen(vsebina_datoteke, a, b):
    seznam = list(map(int, vsebina_datoteke.split(',')))
    seznam[1] = a
    seznam[2] = b
    i = 0
    while seznam[i] != 99:
        if seznam[i] == 1:
            a = seznam[seznam[i+1]]
            b = seznam[seznam[i+2]]
            seznam[seznam[i+3]] = a + b
            i += 4
        elif seznam[i] == 2:
            a = seznam[seznam[i+1]]
            b = seznam[seznam[i+2]]
            seznam[seznam[i+3]] = a * b
            i += 4
    return seznam[0]


def naloga2(vsebina_datoteke):
    resitev = 19690720
    for a in range(100):
        for b in range(100):
            poskus = splosen(vsebina_datoteke, a, b)
            if resitev == poskus:
                break
        if resitev == poskus:
            break

    return str(100*a + b)


if __name__ == '__main__':
    with open('day_2.in', encoding='utf-8') as f:
        vsebina_datoteke = f.read()
    odgovor1 = naloga1(vsebina_datoteke)
    with open('day_2_1.out', 'w', encoding='utf-8') as f:
        f.write(odgovor1)
    odgovor2 = naloga2(vsebina_datoteke)
    with open('day_2_2.out', 'w', encoding='utf-8') as f:
        f.write(odgovor2)