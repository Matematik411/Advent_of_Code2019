def naloga1():
    razpon = (125730,579381)
    prave = 0
    for x in range(razpon[0], razpon[1]):
        enacaj = False
        vecanje = True
        for i, a in enumerate(str(x)):
            if i != (len(str(x)) - 1):
                if a == str(x)[i + 1]:
                    enacaj = True
                if a > str(x)[i + 1]:
                    vecanje = False
                    break
        if (enacaj, vecanje) == (True, True):
            prave += 1
    return str(prave)

def naloga2():
    razpon = (125730,579381)
    prave = 0
    for x in range(razpon[0], razpon[1]):
        enacaj = False
        vecanje = True

        for i, a in enumerate(str(x)):
            if i != (len(str(x)) - 1):
                if a > str(x)[i + 1]:
                    vecanje = False
                    break
                if a == str(x)[i + 1]:
                    fail = False
                    if (i-1) >= 0: 
                        if a == str(x)[i-1]:
                            fail = True
                    if (i+2) < len(str(x)):    
                        if a == str(x)[i+2]:
                            fail = True
                    if not fail:
                        enacaj = True

        if (enacaj, vecanje) == (True, True):
            prave += 1
    return str(prave)


if __name__ == '__main__':
    odgovor1 = naloga1()
    with open('day_4_1.out', 'w', encoding='utf-8') as f:
        f.write(odgovor1)
    odgovor2 = naloga2()
    with open('day_4_2.out', 'w', encoding='utf-8') as f:
        f.write(odgovor2)