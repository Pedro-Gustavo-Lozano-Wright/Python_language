
def funcion_en_una_variable():

    def select_oper(oper):
        def Sum(val1, val2):
            return val1 + val2

        def Mul(val1, val2):
            return val1 * val2

        if oper == 'suma':
            return Sum
        elif oper == 'multiplicacion':
            return Mul

    funcion = select_oper("suma")
    print(funcion(3, 4))


def funcion_multiple_retutn():

    def multi_return():
        return 1, 2, 3

    v1, v2, v3 = multi_return()
    print(v1, v2, v3, )

