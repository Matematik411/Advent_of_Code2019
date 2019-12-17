def naloga1(vsebina_datoteke):
    seznam = sum(list(map(lambda x: (x//3) - 2,map(int, vsebina_datoteke.split()))))
    # vsota = 0
    # for a in seznam:
    #     vsota += (a//3 - 2)
    return str(seznam)

# def naloga2(vsebina_datoteke):
#     seznam = list(map(int, vsebina_datoteke.split()))
#     vsota = 0
#     for a in seznam:
#         posamezni = (a // 3) - 2
#         while posamezni > 0:
#             vsota += posamezni
#             posamezni = (posamezni // 3) - 2

#     return str(vsota)


if __name__ == '__main__':
    with open('day_13.in', encoding='utf-8') as f:
        vsebina_datoteke = f.read()
    odgovor1 = naloga1(vsebina_datoteke)
    with open('day_13_1.out', 'w', encoding='utf-8') as f:
        f.write(odgovor1)
    # odgovor2 = naloga2(vsebina_datoteke)
    # with open('day_13_2.out', 'w', encoding='utf-8') as f:
    #     f.write(odgovor2)