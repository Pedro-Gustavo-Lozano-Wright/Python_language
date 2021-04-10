
def contador_wile():
    count = 0
    while (count < 9):
        print('count is:', count)
        count = count + 1
    else:
        print(count, ", is out")
        print(" un while con else... ahora ya lo he visto todo")
    # break # continue

    # c = a + b assigns value of a + b into c
    # c += a is equivalent to c = c + a
    # c -= a is equivalent to c = c - a
    # c *= a is equivalent to c = c * a
    # c /= a is equivalent to c = c / a
    # c %= a is equivalent to c = c % a
    # c **= a is equivalent to c = c ** a
    # c //= a is equivalent to c = c // a


def funcion_if_else():
    if not (0): print("not() devuelve un bool")

    var0 = 0
    if var0:
        print("esto no se va a imprimir")
    else:
        print("0 es falce")

    var = 1
    if var == 2:
        print("2")
    elif var == 1:
        print("1")
    else:
        print("nada")

        # ==
        # !=
        # >
        # <
        # >=
        # <=
        #


def operaciones():
    print(5 ** 2)
    print(5 ^ 182)  # no se que hace
    print((4 - (2 + 1)) / 2)
    print(round(34 / 67, 2))
    print(9 // 10)  # despues de dividir debuelve solo la parte de los enteros
    print(78 % 60)  # debu3lv2 flaccion pero no funiona
