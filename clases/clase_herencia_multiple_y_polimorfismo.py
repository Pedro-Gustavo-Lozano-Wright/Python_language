
class Classe_A:

  def __init__(self, fruta):
    self.fruta = fruta
    print("Soy de clase A", fruta)

  def metodo_a(self):
    print("Este es el método de A", self.fruta)

  def metodo_polimorfismo(self):
    print("metodo polimorfismo de la classe A")


class Classe_B:

  def __init__(self, verdura):
    self.verdura = verdura
    print("Soy de clase B", verdura)

  def metodo_b(self):
    print("Este es el método de B", self.verdura)

  def metodo_polimorfismo(self):
    print("metodo polimorfismo de la classe B")


class Classe_C(Classe_A, Classe_B): # se le da la priorudad principal a la primera clase escrita
  def __init__(self, fruta, verdura, cereales):
    Classe_A.__init__(self, fruta)#         super().__init__(...)
    Classe_B.__init__(self, verdura)
    self.cereales = cereales
    print("Soy de clase C", cereales)

  def metodo_c(self):
    print("Este es el método de C", self.cereales)

  def metodo_polimorfismo(self):
    print("metodo polimorfismo de la classe C")

def llamar_a_metodo_polimorfismo(classe_a_b_c):
  classe_a_b_c.metodo_polimorfismo()


'''
import pickle
class clase_de_clase:
  lista_de_objetos = []
  def  __init__(self):
    archivo_lisa_de_objetos = open("archivo","ab+")# un archivo binario permite guardar clases
    archivo_lisa_de_objetos.seek(0)
    try:
      self.lista_de_objetos = pickle.load(archivo_lisa_de_objetos)
    except:
      print("no hay nada")
    finally:
      archivo_lisa_de_objetos.close()
      del(archivo_lisa_de_objetos)
  def agregar_objetos(self, objeto):
    self.lista_de_objetos.append(objeto)
    self.guardar_lista_en_archivo()
  def mostrar_lista (self):
    for obj in self.lista_de_objetos:
      print(obj)
  def guardar_lista_en_archivo (self):
    archivo_lisa_de_objetos = open("demofile4.txt", "wb")
    pickle.dump(self.lista_de_objetos, archivo_lisa_de_objetos)  # guardar
    archivo_lisa_de_objetos.close()
    del (archivo_lisa_de_objetos)


#funcion clonada
def hola():
  def decir_hola():
    return("decir hola")
  return decir_hola()

bienvenido = hola()
#bienvenido






numeros = [2, 5, 10, 23, 50, 33]
list( map(lambda x: x*2, numeros) )

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]
list( map(lambda x,y : x*y, a,b) ) #[7, 9, 11, 13, 15]

personas = [Persona("Juan", 35),Persona("Marta", 16),Persona("Manuel", 78),Persona("Eduardo", 12)]
personas = map(lambda p: Persona(p.nombre, p.edad+1), personas)
for persona in personas:
    print(persona)



import inspect

for name, data in inspect.getmembers(instance, inspect.isclass):
    if name.startswith('__'):
        continue
    print('{} : {!r}'.format(name, data))










class Persona_Descriptor:
  def __init__(self, value="j", value2="g"):
    self._value = value
    self._value2 = value2
    print('Creating values')

    # getting the values

  @property
  def value(self):
    print('Getting value')
    return self._value

  @property
  def value2(self):
    print('Getting value2')
    return self._value2

  @value.setter
  def value(self, value):
    print('Setting value to ' + value)
    self._value = value

  @value2.setter
  def value2(self, value2):
    print('Setting value2 to ' + value2)
    self._value2 = value2

  @value.deleter
  def value(self):
    print('Deleting value')
    del self._value

  @value2.deleter
  def value2(self):
    print('Deleting value2')
    del self._value2


x = Persona_Descriptor('Peter', "Gustaf")
print("")
algo = x.value
algo2 = x.value2
print("")
x.value = 'Pit'
x.value2 = 'Gus'
print("")
del x.value
del x.value2




class Persona:
    def __init__(self, value0 = "a", value1 = "b", value2 = "c"):
        self.value0 = value0#publico
        self._value1 = value1# protejido
        self.__value2 = value2# privado
        print('Creating values')

x = Persona('Peter')
#algo = x._Persona__get__
print(x.value0)#publico
print(x._value1)# protejido
print(x._Persona__value2)# privado
'''