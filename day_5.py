def naloga1(vsebina_datoteke, vnos):
    seznam = list(map(int, vsebina_datoteke.split(",")))
    x = vnos
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
            seznam[seznam[i+1]] = x
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
            
            elif opt == 3:
                a = seznam[i+1]
                seznam[a] = x
                i += 2
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

    return str(output)



if __name__ == '__main__':
    with open('day_5.in', encoding='utf-8') as f:
        vsebina_datoteke = f.read()
    odgovor1 = naloga1(vsebina_datoteke, 1)
    with open('day_5_1.out', 'w', encoding='utf-8') as f:
        f.write(odgovor1)
    odgovor2 = naloga1(vsebina_datoteke, 5)
    with open('day_5_2.out', 'w', encoding='utf-8') as f:
        f.write(odgovor2)