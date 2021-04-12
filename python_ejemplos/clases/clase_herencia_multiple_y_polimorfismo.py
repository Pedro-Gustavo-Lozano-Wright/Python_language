
def polimorfismo_y_herencia():
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

  class Classe_C(Classe_A, Classe_B):  # se le da la priorudad principal a la primera clase escrita
    def __init__(self, fruta, verdura, cereales):
      Classe_A.__init__(self, fruta)  # super().__init__(...)
      Classe_B.__init__(self, verdura)
      self.cereales = cereales
      print("Soy de clase C", cereales)

    def metodo_c(self):
      print("Este es el método de C", self.cereales)

    def metodo_polimorfismo(self):
      print("metodo polimorfismo de la classe C")

  def llamar_a_metodo_polimorfismo(classe_a_b_c):
    classe_a_b_c.metodo_polimorfismo()

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
