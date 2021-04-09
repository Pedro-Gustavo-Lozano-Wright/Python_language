
def decorador_envuelve_a_clase():

    def decorador(func):  #
        def nueva_funcion(self, parametro):
            # el decorador roba los argumentos de la func
            # siempre que esten escritos en orden
            print("---", parametro)  # añadir algo
            func(self, parametro)
            print("---", parametro)  # añadir algo

        return nueva_funcion  #

    class perro(object):  #

        def __init__(self, nombre):  #
            self.nombre = nombre  #

        @decorador  #
        def func_a(self, mensaje):  #
            self.mensaje = mensaje  #
            print(self.nombre)
            print(mensaje)
            print("func_a")

        @decorador  #
        def func_b(self, mensaje):  #
            self.mensaje = mensaje  #
            print(mensaje)
            print("func_b")

    maty = perro('Maty') #
    maty.func_a(':)')  #




def classe_como_decorador():
    class miClasseDecorador():
        def __init__(self, func):  # Damos como parámetro una función
            print("1 - new classe")
            self.func = func  # La almacenamos en el constructor
            # la funcion se convirtio en una variable de la classe

        def __call__(self, *args, **kargs):
            print("args", args)
            print("kargs", kargs)
            print("3 - llamada automatica mediante call")
            self.func(*args, **kargs)  # Ejecutamos la funcion en call

    @miClasseDecorador
    def mensaje(mensaje):
        print("4 - cuerpo de la funcion")

    mensaje("2 - Soy un argumento")
