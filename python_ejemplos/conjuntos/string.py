
def funcion_regular_expression():
    import re  # Regular Expression
    txt = "The rain in Spain"
    space_x = re.search("\s", txt)
    print("The first space is in position:", space_x.start())
    # dividir en una lista
    z = re.split("\s", txt)
    print(z)


def funcion_maneras_imprimir():
    a = 3
    print(f"variable a = {a} ")

    var_1 = 19
    var_2 = 26
    var_3 = 30
    ordern = "variable 1: {} variable 2: {} variable 3: {} :)"
    orden_inverso = "ultimo {2} segundo {1} primerp {0}"
    print(ordern.format(var_1, var_2, var_3))
    print(orden_inverso.format(var_1, var_2, var_3))


def ahorro_de_listas():
    # ahorro de listas
    lista = [letra for letra in 'casa']
    print(lista)

    lista = [numero * 2 for numero in range(0, 11)]
    print(lista)

    lista = [numero for numero in range(0, 11) if numero % 2 == 0]
    print(lista)

    # potencias pares de 2
    lista = [numero for numero in
             [numero ** 2 for numero in range(0, 11)]
             if numero % 2 == 0]
    print(lista)


def siclos_con_listas():
    fruits_list = ['banana', 'apple', 'mango']
    for fruit_elemento in fruits_list:  # Second Example
        print('Current fruit :', fruit_elemento)

    fruits = ['banana', 'apple', 'mango']
    for index in range(len(fruits)):
        print('Current fruit :', fruits[index])


