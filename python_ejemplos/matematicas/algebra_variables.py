
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


