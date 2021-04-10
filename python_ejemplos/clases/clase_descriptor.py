
def funcion_descriptor():
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