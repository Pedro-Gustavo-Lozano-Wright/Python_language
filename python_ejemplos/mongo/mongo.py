#instalar
#$ python -m pip install pymongo

'''

from pymongo import MongoClient
from Futbolista import Futbolista

# Creo una lista de objetos futbolista a insertar en la BD
futbolistas = [
  Futbolista('Gus','Loz',33,['Def'],True),
  Futbolista('Carles','Puyol',36,['Central', 'Lateral'],True),
  Futbolista('Sergio','Ramos',28,['Lateral','Central'],True),
  Futbolista('Andrés','Iniesta',30,['Centrocampista','Delantero'],True),
  Futbolista('Fernando','Torres',30,['Delantero'],True),
  Futbolista('Leo','Baptistao',22,['Delantero'],False)
]
#https://www.google.com/search?q=indice+mongodb&oq=indice+mongo&aqs=chrome.0.0j69i57j0i22i30l8.13507j0j7&sourceid=chrome&ie=UTF-8
#https://docs.mongodb.com/manual/indexes/
#https://es.wikipedia.org/wiki/%C3%81rbol-B

def leer():
    # Leemos todos los documentos de la base de datos
    lista_de_futbolistas = collection.find()  # esto significa que se buscan/traen a todof los elementos
    #collection.find({},{nombre:1,apellidos:0)   #primer parentesis bacio indica buscar all y el segundo es traer solo un submenu
    # print(type(lista_de_futbolistas))
    # print("  ")
    for fut in lista_de_futbolistas:
        print("%s - %s - %i - %s - %r" \
              % (fut['nombre'], fut['apellidos'], fut['edad'], fut['demarcacion'], fut['internacional']))

def anadir():
  # añadir los objetos futbolista en la coleccion Futbolista
  for futbolista in futbolistas:
    collection.insert_one(futbolista.toDBCollection())

def leer_filtro():
  # Hacemos una Query con condiciones y lo pasamos a un objeto Futbolista
  # print ("\n\n*** Buqueda de los futbolistas que sean delanteros ***")
  lista_de_futbolistas = collection.find({"demarcacion": {"$in": ["Delantero"]}})
   # collection.find({"nombre_de_la_lista.0": 3})  encontrar un elemrnto especifico en una lista
  for fut in lista_de_futbolistas:
    print("%s - %s - %i - %s - %r" \
      % (fut['nombre'], fut['apellidos'], fut['edad'], fut['demarcacion'], fut['internacional']))

def actualizar():
  # Actualizamos la edad de los jugadores.
  collection.update_many({"edad":{"$gt":30}},{"$inc":{"edad":100}}, upsert = False)
# {"edad":{"$gt":30}} mas de 30 {"edad":30} exactamente 30
#"edad":{"$elemMatch":{"$gt":20}},{"$lt":40}}}} varias condicionrs
# limit... ?
#{$or: [{key1:valor1,ley2:valor2}]}
#"$set" Cambiar a...

def  borrar():
  # Borramos todos los futbolistas que sean internacionales (internacional = true)
  collection.delete_many({"nombre": "Leo"})


mongoClient = MongoClient('localhost')#,27017)# Conexión al Server de MongoDB Pasandole el host y el puerto
print(mongoClient.list_database_names())
db = mongoClient.Fut#  Conexión a la base de datos
collection = db.Futbolistas# Obtenemos una coleccion para trabajar con ella
lista_de_futbolistas = collection.find()
print(lista_de_futbolistas)
#collection.delete_many({"nombre": "Leo"})
mongoClient.close()# Cerrar la conexion



Operadores de consulta de comparación
$eq
Coincide con valores que son iguales a un valor especificado.
$gt
Coincide con valores que son mayores que un valor especificado.
$gte
Coincide con valores que son mayores o iguales a un valor especificado.
$in
Coincide con cualquiera de los valores especificados en una matriz.
$lt
Coincide con valores que son menores que un valor especificado.
$lte
Coincide con valores que son menores o iguales a un valor especificado.
$ne
Coincide con todos los valores que no son iguales a un valor especificado.
$nin
No coincide con ninguno de los valores especificados en una matriz.


Operadores de consultas lógicas
$and
Une cláusulas de consulta con una lógica ANDdevuelve todos los documentos que cumplen las condiciones de ambas cláusulas.
$not
Invierte el efecto de una expresión de consulta y devuelve documentos que no coinciden con la expresión de consulta.
$nor
Une cláusulas de consulta con una lógica NORdevuelve todos los documentos que no coinciden con ambas cláusulas.
$or
Une cláusulas de consulta con una lógica ORdevuelve todos los documentos que cumplen las condiciones de cualquiera de las cláusulas.


Operadores de consulta de elementos
$exists
Coincide con documentos que tienen el campo especificado.
$type
Selecciona documentos si un campo es del tipo especificado.



Actualizar operadores ¶
db.collection.update() db.collection.findAndModify().
Campos
$currentDate
Establece el valor de un campo en la fecha actual, ya sea como Fecha o Marca de tiempo.
$inc
Incrementa el valor del campo en la cantidad especificada.
$min
Solo actualiza el campo si el valor especificado es menor que el valor del campo existente.
$max
Solo actualiza el campo si el valor especificado es mayor que el valor del campo existente.
$mul
Multiplica el valor del campo por la cantidad especificada.
$rename
Cambia el nombre de un campo.
$set
Establece el valor de un campo en un documento.
$setOnInsert
Establece el valor de un campo si una actualización da como resultado la inserción de un documento. No tiene ningún efecto sobre las operaciones de actualización que modifican documentos existentes.
$unset
Elimina el campo especificado de un documento.
Matriz
Operadores1
$
Actúa como un marcador de posición para actualizar el primer elemento que coincide con la condición de la consulta.
$[]
Actúa como un marcador de posición para actualizar todos los elementos de una matriz para los documentos que coinciden con la condición de la consulta.
$[<identifier>]
Actúa como un marcador de posición para actualizar todos los elementos que coinciden con la arrayFilterscondición de los documentos que coinciden con la condición de la consulta.
$addToSet
Agrega elementos a una matriz solo si aún no existen en el conjunto.
$pop
Elimina el primer o último elemento de una matriz.
$pull
Elimina todos los elementos de la matriz que coinciden con una consulta especificada.
$push
Agrega un elemento a una matriz.
$pullAll
Elimina todos los valores coincidentes de una matriz.
Modificadores
$each
Modifica los operadores $pushy $addToSetpara agregar varios elementos para las actualizaciones de la matriz.
$position
Modifica el $pushoperador para especificar la posición en la matriz para agregar elementos.
$slice
Modifica el $pushoperador para limitar el tamaño de las matrices actualizadas.
$sort
Modifica el $pushoperador para reordenar los documentos almacenados en una matriz.
Bit a bit
Nombre
Descripción
$bit
Realiza actualizaciones bit a bit AND, ORy XORde valores enteros.
'''
