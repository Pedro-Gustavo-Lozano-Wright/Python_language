
def string_como_lista():# los strings son listas
    word = 'Python'
    print(word[0], word[-6])
    print(word[-1],  word[5])  # seleccionar caracter desdel final empieza en -1
    print(word[0:2])  # cadena segmento
    print(word[3:6])  # cadena setmento
    print(word[:2])  # cadena de un extremo a un punto
    print(word[2:])
    print(word[-2:])  # cadena desde el penu ltimo

def lista_basico():# las listas son editables
    list = ['abcd', 786, 2.23, 'john', 70.2, 'abcd']# CORCHETES
    list_num = [123, 23, 252]

    print(list)  # Prints complete list
    print(list[0])  # Prints first elelent of the list
    print(list[1:3])  # Prints elements starting from 2nd till 3rd
    print(list[2:])  # Prints elements starting from 3rd element
    print(list_num * 2)  # Prints list two times
    print(list + list_num)  # Prints concatenated lists

    print("la lista tiene ", len(list), "elementos")  # find length of list
    print("encontrar el index del elemento john...  index" ,list.index("john"))  # find index of element that occurs first
    print("cuantas veces esta el termino abcd...", list.count('abcd'))  # find count of the element
    print("ver lista ordenada")
    print(sorted(list_num))  # print sorted list but not change original
    list_num.sort(reverse=True)
    print(list_num)# sort original list

def tupla_aburrido():    # tupla no se edita
    tuple = ('abcd', 786, 2.23, 'john', 70.2)# PARENTECIS
    lista = list(tuple)
    print(lista)

#  usa corchetes igual que set()
def diccionario_basico():    # un diccionario es un json y son una tabla hash Los diccionarios no tienen concepto de orden entre elementos
    dicc = {'uno': 1, 'dos': 2, 'tres': 3, 'name': 'john', 'code': 34}
    dicc_2 = dict({'uno': 1, 'dos': 2, 'tres': 3})
    dicc_3 = dict(uno=1, dos=2, tres=3)
    print(dicc)
    dicc['uno'] = "This is one"  # no se encontro, por eso se agrego alfinal
    dicc['name'] = "Gus"  # si se encotro y se cambio
    dicc[2] = "This is two"
    print(dicc)  # Prints complete dictionary
    print(dicc['uno'])  # Prints value for 'one' key
    print(dicc[2])  # Prints value for 2 key
    print(dicc)  # Prints complete dictionary
    print(dicc.keys())  # Prints all the keys
    print(dicc.values())  # Prints all the values

#  usa corchetes igual que dict()
def set_basico():# no permite elementos duplicados
    lista = ['a', 'b', 'c', 'd']  # convertir de uno a otro
    conjunto = set(lista)  # diccionario con value vacio
    conjunto.add('tres')
    conjunto.add('estoy desordenado')
    print(conjunto)

def diccionarios_json():
    G = {'z': {'z1': 1, 'z2': 2},
         'x': {'x1': 3, 'x2': "4 encontraste un dato anidado"},
         'y': {'y1': 5, 'y2': 6}}

    print(G["x"]["x2"])

    for dato in G.values():
        for k, v in dato.items():
            print(k, v)
        print("-")



#La función append () agrega los elementos como un solo elemento.
#La función extend () agrega los elementos uno por uno a la lista.
#La función insert () agrega el elemento
#Para eliminar elementos por el index use "del"
#Para eliminar un elemento por su valor, use remove ().
#Si extraer/cortar el elemento use pop
#para borrar la lista entera use clear()
