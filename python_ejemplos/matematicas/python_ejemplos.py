from python_ejemplos.clases.clase_descriptor import Persona_Descriptor
from python_ejemplos.clases.clase_herencia_multiple_y_polimorfismo import Classe_B, Classe_C, Classe_A, \
    llamar_a_metodo_polimorfismo
from python_ejemplos.clases.clases_simple import Person_abstracta, Person_estudiante
from python_ejemplos.conjuntos.basicos import string_como_lista, lista_basico, tupla_aburrido, diccionario_basico, \
    set_basico, diccionarios_json
from python_ejemplos.conjuntos.especiales import funcion_lambda, funcion_map, funcion_listas_y_lambda, funcion_yield, \
    funcion_on_demand
from python_ejemplos.conjuntos.string import funcion_regular_expression, funcion_maneras_imprimir, ahorro_de_listas, \
    siclos_con_listas
from python_ejemplos.funciones.decoradores import funcion_ejemplo_dec, funcion_decorador_argumentos
from python_ejemplos.funciones.decoradores_con_classes import decorador_envuelve_a_clase, classe_como_decorador
from python_ejemplos.funciones.funciones_basicas import funcion_en_una_variable, funcion_multiple_retutn
from python_ejemplos.matematicas.algebra_variables import operaciones_boleanas
from python_ejemplos.matematicas.logica import contador_wile
from python_ejemplos.sistema.errores import errores
from python_ejemplos.storage.file_binario import guardar_objetos_en_archivo
from python_ejemplos.storage.file_txt import crear_texto_simple, leer_texto_simple, add_line_texto_simple, \
    add_texto_simple, borrar_texto_simple


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
    funcion_lambda()
    print("")
    funcion_map()
    print("")
    funcion_listas_y_lambda()
    print("")
    funcion_yield()
    print("")
    funcion_on_demand()

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

    car = {"brand": "Ford", "year": 1964}
    dic_x = car.items()
    print(dic_x)        # before the change
    car["year"] = 2020  # la variable y el diccionario estan conectados, se actualiza igualmente
    print(dic_x)        # after the change
    print("las variables estan conectadas")          # after the change

def guardar_file():
    crear_texto_simple()
    leer_texto_simple()
    add_line_texto_simple("otra linea")
    add_texto_simple("text_add")
    borrar_texto_simple()
    #import os #borrar carpeta
    #os.rmdir("myfolder")

def guardar_file_bin():
    objeto_bin = guardar_objetos_en_archivo()
    gustavo = Person_abstracta("aa", "bb", 24)
    objeto_bin.agregar_objetos(gustavo)
    objeto_bin.mostrar_lista()

def ejemplos_conjuntos():
    string_como_lista()
    lista_basico()
    tupla_aburrido()
    diccionario_basico()
    set_basico()
    diccionarios_json()

def matematica_boleana():
    operaciones_boleanas()
    contador_wile()

def funciones_especiales():
    funcion_en_una_variable()
    funcion_multiple_retutn()
    funcion_ejemplo_dec()
    funcion_decorador_argumentos()
    decorador_envuelve_a_clase()
    classe_como_decorador()

def fuciones_string():
    funcion_regular_expression()
    funcion_maneras_imprimir()
    ahorro_de_listas()
    siclos_con_listas()

def sistema_tools():
    errores()


''''''