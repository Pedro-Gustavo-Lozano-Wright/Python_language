
def funcion_ejemplo_dec():

    def decorador_add_codigo(func,):  # se recibe (B) dentro de (A)
        def nueva_funcion():  # función (C) que se devolvera
            print("---")  # Añadimos algo
            func()  # Aquí esta la función (B)
            print("---")  # Añadimos algo
        return nueva_funcion  # Para devolver (C)

    # cuando la funcion va con parentecis se ejecuta,
    # sin parentecis se convierte en variable

    @decorador_add_codigo  # "Decoramos" la función
    def func1():
        print("Gus!")

    @decorador_add_codigo  # "Decoramos" la función
    def func2():
        print("Tavo")

    func1()#decoradores sin parametro
    func2()

def funcion_decorador_argumentos():

    def seleccion(operacion, val1, val2):
        if operacion == 'suma':
            return Sumar(val1, val2)
        if operacion == 'multiplicacion':
            return Multiplicacion(val1, val2)

    def Sumar(val1, val2):
        return val1 + val2

    def Multiplicacion(val1, val2):
        return val1 * val2

    print(seleccion('suma', 5.0, 3))
    print(seleccion('multiplicacion', 5.0, 3))


def decoradores_anidados():
    def star(func):
        def inner(*args, **kwargs):
            print("*" * 30)
            func(*args, **kwargs)
            print("*" * 30)

        return inner

    def percent(func):
        def inner(*args, **kwargs):
            print("%" * 30)
            func(*args, **kwargs)
            print("%" * 30)

        return inner

    @star
    @percent
    def printer(msg):
        print(msg)

    printer("Hello")