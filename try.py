def postopek(vsebina_datoteke, vnos):
    seznam = list(map(int, vsebina_datoteke.split(",")))

    output = 0
    i = 0
    baza = 0

    while seznam[i] != 99:
        try:
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
                seznam[seznam[i+1]] = vnos
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
            elif seznam[i] == 9:
                baza += seznam[seznam[i]]
                i += 2

            else:
                opt = seznam[i] % 100
                m1 = (seznam[i] // 100) % 10  
                m2 = (seznam[i] // 1000) % 10
                m3 = (seznam[i] // 10000) % 10
                if opt in [1, 2, 7, 8]:
                    if m1 == 0:
                        a = seznam[seznam[i+1]]
                    elif m1 == 1:
                        a = seznam[i+1]
                    else:
                        a = seznam[seznam[i+1] + baza]

                    if m2 == 0:
                        b = seznam[seznam[i+2]]
                    elif m2 == 1:
                        b = seznam[i+2]
                    else:
                        b = seznam[seznam[i+2] + baza]


                    if opt == 1:
                        if m3 == 0:
                            seznam[seznam[i+3]] = a + b
                        elif m3 == 1:                        
                            seznam[i+3]  = a + b
                        else:
                            seznam[seznam[i+3] + baza] = a + b

                    elif opt == 2:
                        if m3 == 0:
                            seznam[seznam[i+3]] = a * b
                        elif m3 == 1:
                            seznam[i+3]  = a * b
                        else:
                            seznam[seznam[i+3] + baza] = a * b


                    elif opt == 7:
                        if m3 == 0:
                            if a < b:
                                seznam[seznam[i+3]] = 1
                            else:
                                seznam[seznam[i+3]] = 0

                        elif m3 == 1:
                            if a < b:
                                seznam[i+3]  = 1
                            else:
                                seznam[i+3]  = 0
                        
                        else:
                            if a < b:
                                seznam[seznam[i+3] + baza] = 1
                            else:
                                seznam[seznam[i+3] + baza] = 0


                    elif opt == 8:
                        if m3 == 0:
                            if a == b:
                                seznam[seznam[i+3]] = 1
                            else:
                                seznam[seznam[i+3]] = 0
                        elif m3 == 1:
                            if a == b:
                                seznam[i+3]  = 1
                            else:
                                seznam[i+3]  = 0
                        else:
                            if a == b:
                                seznam[seznam[i+3] + baza] = 1   
                            else:
                                seznam[seznam[i+3] + baza] = 0     
                    i += 4

                elif opt in [4, 9]:
                    if m1 == 0:
                        a = seznam[seznam[i+1]]
                    elif m1 == 1:
                        a = seznam[i+1]
                    else:
                        a = seznam[seznam[i+1] + baza]
                    
                    if opt == 4:
                        output = a
                    else:
                        baza += a
                    i += 2      
                elif opt in [5, 6]:   
                    if m1 == 0:
                        a = seznam[seznam[i+1]]
                    elif m1 == 1:
                        a = seznam[i+1]
                    else:
                        a = seznam[seznam[i+1] + baza]

                    if m2 == 0:
                        b = seznam[seznam[i+2]]
                    elif m2 == 1:
                        b = seznam[i+2]
                    else:
                        b = seznam[seznam[i+2] + baza]    

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
        except IndexError:
            d = len(seznam)
            m = max(seznam[i+1], seznam[i+2], seznam[i+3])
            m = max(m, m + baza)
            for _ in range(m+100, d):
                seznam.append(0)
    return output


def naloga1(vsebina_datoteke):
    return str(postopek(vsebina_datoteke, 1))




if __name__ == '__main__':
    with open('day_9.in', encoding='utf-8') as f:
        vsebina_datoteke = f.read()
    odgovor1 = naloga1(vsebina_datoteke)
    with open('day_9_1.out', 'w', encoding='utf-8') as f:
        f.write(odgovor1)
    # odgovor2 = naloga1(vsebina_datoteke, 5)
    # with open('day_5_2.out', 'w', encoding='utf-8') as f:
    #     f.write(odgovor2)