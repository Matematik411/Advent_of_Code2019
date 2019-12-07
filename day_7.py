def postopek(vsebina_datoteke, faza, vnos):
    seznam = list(map(int, vsebina_datoteke.split(",")))
    output = 0
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
        elif seznam[i] == 3:
            seznam[seznam[i+1]] = faza
            faza = vnos
            i += 2

        elif seznam[i] == 4:
            a = seznam[seznam[i+1]]
            output = a
            i += 2
        elif seznam[i] == 5:
            if seznam[seznam[i+1]] != 0:
                i = seznam[seznam[i+2]]
            else:
                i += 3
        elif seznam[i] == 6:
            if seznam[seznam[i+1]] == 0:
                i = seznam[seznam[i+2]]
            else:
                i += 3
        elif seznam[i] == 7:
            if seznam[seznam[i+1]] < seznam[seznam[i+2]]:
                seznam[seznam[i+3]] = 1
            else:
                seznam[seznam[i+3]] = 0
            i += 4
        elif seznam[i] == 8:
            if seznam[seznam[i+1]] == seznam[seznam[i+2]]:
                seznam[seznam[i+3]] = 1
            else:
                seznam[seznam[i+3]] = 0
            i += 4

        
        else:
            opt = seznam[i] % 100
            m1 = (seznam[i] // 100) % 10  
            m2 = (seznam[i] // 1000) % 10
            m3 = (seznam[i] // 10000) % 10
            if opt in [1, 2, 7, 8]:
                if m1 == 0:
                    a = seznam[seznam[i+1]]
                else:
                    a = seznam[i+1]

                if m2 == 0:
                    b = seznam[seznam[i+2]]
                else:
                    b = seznam[i+2]

                if opt == 1:
                    if m3 == 0:
                        seznam[seznam[i+3]] = a + b
                    else:
                        
                        seznam[i+3]  = a + b

                elif opt == 2:
                    if m3 == 0:
                        seznam[seznam[i+3]] = a * b
                    else:
                        seznam[i+3]  = a * b

                elif opt == 7:
                    if m3 == 0:
                        if a < b:
                            seznam[seznam[i+3]] = 1
                        else:
                            seznam[seznam[i+3]] = 0

                    else:
                        if a < b:
                            seznam[i+3]  = 1
                        else:
                            seznam[i+3]  = 0

                elif opt == 8:
                    if m3 == 0:
                        if a == b:
                            seznam[seznam[i+3]] = 1
                        else:
                            seznam[seznam[i+3]] = 0
                    else:
                        if a == b:
                            seznam[i+3]  = 1
                        else:
                            seznam[i+3]  = 0
                            
                i += 4

            elif opt == 4:
                if m1 == 0:
                    a = seznam[seznam[i+1]]
                else:
                    a = seznam[i+1]
                output = a
                i += 2      
            elif opt in [5, 6]:   
                if m1 == 0:
                    a = seznam[seznam[i+1]]
                else:
                    a = seznam[i+1]

                if m2 == 0:
                    b = seznam[seznam[i+2]]
                else:
                    b = seznam[i+2]    

                if opt == 5:
                    if a != 0:
                        i = b
                    else:
                        i += 3
                else:
                    if a == 0:
                        i = b
                    else:
                        i += 3 

    return output


def naloga1(vsebina_datoteke):
    resitev = 0
    for moznost in itertools.permutations([0, 1, 2, 3, 4]):
        vnos = 0
        for x in moznost:
            vnos = postopek(vsebina_datoteke, x, vnos)
        resitev = max(vnos, resitev)

    return str(resitev)  # (2, 4, 3, 0, 1)


def amp(data): # [seznam, i, vnos] -> [a, seznam, i, vnos]
    seznam, i, vnos = data
    seznam = seznam[::]


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
        elif seznam[i] == 3:
            seznam[seznam[i+1]] = vnos[0]
            vnos = vnos[1:]
            i += 2

        elif seznam[i] == 4:
            a = seznam[seznam[i+1]]
            i += 2
            if seznam[i-1] == 99:
                return ["konec", a]
            else:    
                return [a, seznam, i, vnos]

        elif seznam[i] == 5:
            if seznam[seznam[i+1]] != 0:
                i = seznam[seznam[i+2]]
            else:
                i += 3
        elif seznam[i] == 6:
            if seznam[seznam[i+1]] == 0:
                i = seznam[seznam[i+2]]
            else:
                i += 3
        elif seznam[i] == 7:
            if seznam[seznam[i+1]] < seznam[seznam[i+2]]:
                seznam[seznam[i+3]] = 1
            else:
                seznam[seznam[i+3]] = 0
            i += 4
        elif seznam[i] == 8:
            if seznam[seznam[i+1]] == seznam[seznam[i+2]]:
                seznam[seznam[i+3]] = 1
            else:
                seznam[seznam[i+3]] = 0
            i += 4

        
        else:
            opt = seznam[i] % 100
            m1 = (seznam[i] // 100) % 10  
            m2 = (seznam[i] // 1000) % 10
            m3 = (seznam[i] // 10000) % 10
            if opt in [1, 2, 7, 8]:
                if m1 == 0:
                    a = seznam[seznam[i+1]]
                else:
                    a = seznam[i+1]

                if m2 == 0:
                    b = seznam[seznam[i+2]]
                else:
                    b = seznam[i+2]

                if opt == 1:
                    if m3 == 0:
                        seznam[seznam[i+3]] = a + b
                    else:
                        
                        seznam[i+3]  = a + b

                elif opt == 2:
                    if m3 == 0:
                        seznam[seznam[i+3]] = a * b
                    else:
                        seznam[i+3]  = a * b

                elif opt == 7:
                    if m3 == 0:
                        if a < b:
                            seznam[seznam[i+3]] = 1
                        else:
                            seznam[seznam[i+3]] = 0

                    else:
                        if a < b:
                            seznam[i+3]  = 1
                        else:
                            seznam[i+3]  = 0

                elif opt == 8:
                    if m3 == 0:
                        if a == b:
                            seznam[seznam[i+3]] = 1
                        else:
                            seznam[seznam[i+3]] = 0
                    else:
                        if a == b:
                            seznam[i+3]  = 1
                        else:
                            seznam[i+3]  = 0
                            
                i += 4

            elif opt == 4:
                if m1 == 0:
                    a = seznam[seznam[i+1]]
                else:
                    a = seznam[i+1]
                i += 2      
                return [a, seznam, i, vnos]


            elif opt in [5, 6]:   
                if m1 == 0:
                    a = seznam[seznam[i+1]]
                else:
                    a = seznam[i+1]

                if m2 == 0:
                    b = seznam[seznam[i+2]]
                else:
                    b = seznam[i+2]    

                if opt == 5:
                    if a != 0:
                        i = b
                    else:
                        i += 3
                else:
                    if a == 0:
                        i = b
                    else:
                        i += 3 






import itertools

def naloga2(vsebina_datoteke):
    resitev = 0
    zacetni = list(map(int, vsebina_datoteke.split(",")))

    for moznost in itertools.permutations([5, 6, 7, 8, 9]):
        a, *rest = moznost

        amps = []
        ampA = [zacetni[::], 0, [a, 0]]
        izhod, *ampA = amp(ampA)
        amps.append(ampA)

        for k in rest:
            motor = [zacetni[::], 0, [k, izhod]]
            izhod, *motor = amp(motor)
            amps.append(motor)
        amps[0][2].append(izhod)


        while True:
            for j in range(5):
                motor = amps[j]
                rezultat = amp(motor)
                izhod, *motor = rezultat
                amps[j] = motor
                if j < 4:
                    amps[j+1][2].append(izhod)
                else:
                    amps[0][2].append(izhod)

            if amp(amps[0]) is None:
                break

        resitev = max(izhod, resitev)
    return str(resitev)


if __name__ == '__main__':
    with open('day_7.in', encoding='utf-8') as f:
        vsebina_datoteke = f.read()
    odgovor1 = naloga1(vsebina_datoteke)
    with open('day_7_1.out', 'w', encoding='utf-8') as f:
        f.write(odgovor1)
    odgovor2 = naloga2(vsebina_datoteke)
    with open('day_7_2.out', 'w', encoding='utf-8') as f:
        f.write(odgovor2)