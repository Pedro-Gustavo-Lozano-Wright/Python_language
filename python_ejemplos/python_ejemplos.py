
from python_ejemplos.clases.clase_descriptor import funcion_descriptor
from python_ejemplos.clases.clase_herencia_multiple_y_polimorfismo import polimorfismo_y_herencia
from python_ejemplos.clases.clases_simple import ejemplo_clase_abstracta, Person_abstracta
from python_ejemplos.clases.operaciones_ecpeciales import operaciones_ecpeciales
from python_ejemplos.clases.polimorfismo_simple import polimorfismo_simple
from python_ejemplos.conjuntos.basicos import string_como_lista, lista_basico, tupla_aburrido, diccionario_basico, \
    set_basico, diccionarios_json
from python_ejemplos.conjuntos.especiales import funcion_lambda, funcion_map, funcion_listas_y_lambda, funcion_yield, \
    funcion_on_demand
from python_ejemplos.conjuntos.string import funcion_regular_expression, funcion_maneras_imprimir, ahorro_de_listas, \
    siclos_con_listas, revicion_string
from python_ejemplos.funciones.decoradores import funcion_ejemplo_dec, funcion_decorador_argumentos, \
    decoradores_anidados
from python_ejemplos.funciones.decoradores_con_classes import decorador_envuelve_a_clase, classe_como_decorador
from python_ejemplos.funciones.funciones_basicas import funcion_en_una_variable, funcion_multiple_retutn
from python_ejemplos.matematicas.algebra_variables import operaciones_boleanas, operaciones_binarias
from python_ejemplos.matematicas.logica import contador_wile, funcion_if_else, operaciones
from python_ejemplos.matematicas.matmaticas import matematicas_general
from python_ejemplos.sistema.errores import errores
from python_ejemplos.sistema.tiempo import funcion_dormir_simple, funcion_hilos, auto_destruccion_de_hilo, \
    funcion_hilos_juntos, funcion_time_out, funcion_hora, hilos_threading
from python_ejemplos.sistema.tkin_graph import funcion_grafica
from python_ejemplos.storage.file_binario import guardar_objetos_en_archivo
from python_ejemplos.storage.file_txt import crear_texto_simple, leer_texto_simple, add_line_texto_simple, \
    add_texto_simple, borrar_texto_simple

def classe_en_python():
    ejemplo_clase_abstracta()
    funcion_descriptor()
    polimorfismo_y_herencia()
    polimorfismo_simple()
    operaciones_ecpeciales()

def lambda_map_y_list():
    funcion_lambda()
    funcion_map()
    funcion_listas_y_lambda()
    funcion_on_demand()
    funcion_yield()

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

    a,b,c = 1,2,"john" #3 variables diferentes
    z = 1 ; del z # eliminar variable

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

def matematicas():
    #operaciones_ecpeciales()# clase de eje de cordenadas
    operaciones_boleanas()
    contador_wile()
    funcion_if_else()
    operaciones()
    operaciones_binarias()
    matematicas_general()

def funciones_especiales():
    funcion_en_una_variable()
    funcion_multiple_retutn()
    funcion_ejemplo_dec()
    funcion_decorador_argumentos()
    decorador_envuelve_a_clase()
    classe_como_decorador()
    decoradores_anidados()

def fuciones_string():
    funcion_regular_expression()
    funcion_maneras_imprimir()
    ahorro_de_listas()
    siclos_con_listas()
    revicion_string()

def sistema_tools():
    errores()
    funcion_grafica()
    hilos_threading()
    #funcion_dormir_simple()
    #funcion_hilos()
    #funcion_hilos_juntos()
    auto_destruccion_de_hilo()
    funcion_time_out()
    funcion_hora()

def base_de_datos():
    pass

