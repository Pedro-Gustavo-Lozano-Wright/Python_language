from design_patterns.creacional import factoria_abstracta, singleton, builder, factori_metod
from design_patterns.estructural import composite, decorador_anadir_capas, observer_subscripcion
from design_patterns.comportamiento import cadena_de_operacion, iterador, state, strategy
from python_ejemplos import python_ejemplos

if __name__ == '__main__':


    factoria_abstracta.ejemplo_factoria_abstracta()
    #objetos con propiedades y constructores abstractas
    singleton.singleton1()
    singleton.singleton2()
    #asegura que una clase tenga una unica instancia global
    builder.ejemplo_builder()
    #construye objetos usando modulos adaptables
    factori_metod.factori_metod()
    #objetos que son alterados por sus subclases
    composite.ejemplo_composite()
    #manejar objetos con estructura de arbol
    decorador_anadir_capas.decorador_anadir_capas()
    #añadir funcionalidades por capas
    cadena_de_operacion.cadena_de_operacion()
    #pasar solicitud en una cadena de objetos
    iterador.ejemplo_iterador()
    #manipular colleccion de objetos iterable
    observer_subscripcion.observer_subscripcion()
    #enviar informacion clases suscritas
    state.state()
    #cambiar acciones segun su estado
    strategy.strategy()
    #algoritmos intercambiables

    python_ejemplos.classe_en_python()
    python_ejemplos.lambda_map_y_list()
    python_ejemplos.guardar_file()
    python_ejemplos.variables()
    python_ejemplos.guardar_file_bin()
    python_ejemplos.ejemplos_conjuntos()
    python_ejemplos.matematicas()
    python_ejemplos.funciones_especiales()
    #python_ejemplos.sistema_tools()
    python_ejemplos.fuciones_string()
    python_ejemplos.base_de_datos()

    '''
    '''
#from folder_name import file_name
#from folder_name import *
# #folder_name.funcion_name()
#debugear con los breackpoits y la catarina verde




