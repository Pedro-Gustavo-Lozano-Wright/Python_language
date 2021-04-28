#lambda_map_list_yield
from python_ejemplos.clases.clases_simple import Person_abstracta

personas = [Person_abstracta("Juan", "", 35),
            Person_abstracta("Marta", "", 16),
            Person_abstracta("Manuel", "", 78),
            Person_abstracta("Eduardo", "", 12)]

def funcion_lambda():
    menores = filter(lambda persona: persona.age < 18, personas)  # filtrar por atributo de la clase
    for menor in menores:
        print(menor.name)

def funcion_map():
    personas_map = map(lambda persona: Person_abstracta(persona.name, persona.age + 1), personas)
    for persona_old in personas_map:
        print(persona_old.name, persona_old.age)

def funcion_listas_y_lambda():
    numeros = [2, 5, 10, 23, 50, 33]
    print(list(map(lambda x: x * 2, numeros)))
    a = [1, 2, 3, 4, 5]
    b = [6, 7, 8, 9, 10]
    print(list(map(lambda x, y: x * y, a, b)))  # [7, 9, 11, 13, 15]

def funcion_yield():  #https://www.programiz.com/python-programming/generator
    def contador(max):
        n = 0
        while n < max:
            yield n  #yield es un return pero sin salirsr de la funcion
            n = n + 1  # yield from es esnviar un sub elemento
    mycont = contador(7)# va devilviendo una lista
    print(list(mycont))
    mycont2 = contador(4)# va devilviendo una lista
    print(mycont)
    print("-")
    print(mycont)
    print("-")
    print(mycont)
    print("-")
    print(mycont)

def mescla_faro_de_listas_zip():
    coordinate = ['x', 'y', 'z']
    value = [3, 4, 5]

    result = zip(coordinate, value)
    result_list = list(result)
    print(result_list)

    c, v = zip(*result_list)
    print('c =', c)
    print('v =', v)


def funcion_on_demand(): #https://www.programiz.com/python-programming/generator
    class on_demand:
        def __iter__(self):
            self.a = 1
            print("iter")
            return self

        def __next__(self):
            x = self.a
            self.a += 1
            print("next")
            return x

    myclass = on_demand()
    myiter = iter(myclass)  # cada vez que se nececita
    # vuelve a la funcion para generar otro dato,
    # bastante util cuando no sabes cuantos datos nececitaras
    print(next(myiter))
    print(next(myiter))
    print(next(myiter))
    print(next(myiter))
    print(next(myiter))
