
class Person_abstracta():
  """esta es el texto de descripcion"""

  def __init__(self,  name="", last = "", age = 0):
      self.__vivo = True  # variabl privada
      self._last = last  # variabl protejida
      self.name = name  # variabl publica
      self.age = age  # variabl publica

  def pedir_self(self):
    return self

  def anadir_edad(self,edad):
    self.age += edad

  def preguntar_nombre(self):
    print("Hola soy " + self.name, self._last)

  def pedir_edad(self):
    return self.age

  def __esta_es_una_funcion_interna(self):
    print("solo puede ser llamada desde la clase")

class Person_estudiante(Person_abstracta):

  def __init__(self, escuela = "escuela_x", name="nombre_x", last="apeido_x", age=0):
    #Person_abstracta.__init__(self,name,last,age)
    super().__init__(name,last,age)
    self.escuela = escuela

  def actualizar_escuela(self,escuela):
    self.escuela = escuela

  def preguntar_escuela(self):
    print(self.escuela)

