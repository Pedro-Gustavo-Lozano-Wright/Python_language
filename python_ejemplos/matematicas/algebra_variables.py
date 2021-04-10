
def operaciones_boleanas():
    # conjuntos para operaciones logicas and or etc
    a = {1, 2, 5, 4.6, 7.8, 'r', 's'}
    b = {2, 5, 'd', 'abc'}
    c = {2, 3, 4, }
    print(a & b)
    print(a & b & c)  # a.intersection(b,c))

    # {2, 5}
    # {2}

    a = {1, 2, 5, 4.6, 7.8, 'r', 's'}
    b = {2, 5, 'd', 'abc'}
    c = {2, 3, 4}
    print(a - b - c)  # a.difference(b,c))
    # {1, 4.6, 7.8, 'r', 's'}


def operaciones_binarias():
    # compuertas loguicas

    a = 60  # 60 = 0011 1100
    b = 13  # 13 = 0000 1101
    c = 0

    c = a & b  # 12 = 0000 1100
    print("Line 1 - Value of c is ", c)

    c = a | b  # 61 = 0011 1101
    print("Line 2 - Value of c is ", c)

    c = a ^ b  # 49 = 0011 0001
    print("Line 3 - Value of c is ", c)

    c = ~a  # -61 = 1100 0011 NOT
    print("Line 4 - Value of c is ", c)

    c = a << 2  # 240 = 1111 0000 RECORRER A LA ISQ
    print("Line 5 - Value of c is ", c)

    c = a >> 2  # 15 = 0000 1111 RECORRER A LA DER
    print("Line 6 - Value of c is ", c)

    print(100 % 8)  # 100 entre 8 es 12.5, si se concideran los enteros una docena cabe 8 veces en el 100 y quedan 4

