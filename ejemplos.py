from clases.clase_descriptor import Persona_Descriptor
from clases.clase_herencia_multiple_y_polimorfismo import \
    Classe_B, Classe_C, Classe_A, \
    llamar_a_metodo_polimorfismo
from clases.clases_simple import Person_abstracta, Person_estudiante
from storage.file_txt import crear_texto_simple, leer_texto_simple, add_texto_simple, borrar_texto_simple, \
    add_line_texto_simple


def clases_simple():
    print(" \n\n-clases_simple\n ")
    gustavo = Person_abstracta("Gus", "Loz", 24)
    print(gustavo.__doc__[0:])
    print("")
    gustavo.name = "Tavo"
    gustavo.preguntar_nombre()
    gustavo.anadir_edad(1)
    print(gustavo.pedir_edad(), "años")
    #gustavo._Person_abstracta__esta_es_una_funcion_interna
    print("")
    gustavo_alumno = Person_estudiante()
    gustavo_alumno.actualizar_escuela("uni")
    gustavo_alumno.preguntar_escuela()
    gustavo_alumno.preguntar_nombre()

def clase_herencia_multiple_y_polimorfismo():
    print(" \n\n-clase_herencia_multiple_y_polimorfismo\n ")
    objeto_de_clase_b = Classe_B("Betabel")  #
    objeto_de_clase_b.metodo_b()
    print("")
    objeto_de_clase_c = Classe_C("arandanos", "brocoli", "cebada")
    objeto_de_clase_c.metodo_a()
    objeto_de_clase_c.metodo_b()
    objeto_de_clase_c.metodo_c()
    print("")
    objeto_de_clase_a = Classe_A("Aguacate")
    objeto_de_clase_a.metodo_polimorfismo()
    # aqui es ejecuta escojiendo el objeto
    print("")
    llamar_a_metodo_polimorfismo(objeto_de_clase_a)
    llamar_a_metodo_polimorfismo(objeto_de_clase_b)
    llamar_a_metodo_polimorfismo(objeto_de_clase_c)
    # aqui es ejecuta escojiendo el metodo

def lambda_map_y_list():
    print(" \n\n-lambda_map_y_list\n ")
    personas = [Person_abstracta("Juan", "", 35),
                Person_abstracta("Marta", "", 16),
                Person_abstracta("Manuel", "", 78),
                Person_abstracta("Eduardo", "", 12)]

    menores = filter(lambda persona: persona.age < 18, personas)  # filtrar por atributo de la clase
    for menor in menores:
        print(menor.name)
    print("")
    personas_map = map(lambda persona: Person_abstracta(persona.name, persona.age + 1), personas)
    for persona_old in personas_map:
        print(persona_old.name, persona_old.age)
    print("")
    numeros = [2, 5, 10, 23, 50, 33]
    print(list(map(lambda x: x * 2, numeros)))
    print("")
    a = [1, 2, 3, 4, 5]
    b = [6, 7, 8, 9, 10]
    print(list(map(lambda x, y: x * y, a, b)))  # [7, 9, 11, 13, 15]

def elementos_de_clase_con_inspect():
    print(" \n\n-elementos_de_clase_con_inspect\n ")

    gustavo = Person_abstracta("Gus", "Loz", 24)

    import inspect

    for name, data in inspect.getmembers(gustavo):
        if name.startswith('__'):
            continue
        print('{} : {!r}'.format(name, data))

def descriptores_geter_y_seter_mod():
    print(" \n\n-descriptores_geter_y_seter_mod\n ")
    persona_simple = Persona_Descriptor('Peter', "Gustaf")
    print("")
    algo = persona_simple.value
    algo2 = persona_simple.value2
    print("")
    persona_simple.value = 'Pit'
    persona_simple.value2 = 'Gus'
    print("")
    del persona_simple.value
    del persona_simple.value2

def guardar_file():
    crear_texto_simple()
    leer_texto_simple()
    add_line_texto_simple("otra linea")
    add_texto_simple("text_add")
    borrar_texto_simple()

def variables():
    variable_global_x = 300
    def myfunc():
        global variable_global_x #forzar variable global
        variable_global_x = 200
    myfunc()
    print(variable_global_x)

    variable_z = 300
    def myfunc():
        variable_z = 200 #solo es global
        # cuando no parece que es una nueva
        # variable con el mismo nombre
        print(variable_z)
    myfunc()
    print(variable_z)
