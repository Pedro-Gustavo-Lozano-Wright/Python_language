
file_name = "texto_simple.txt"
lista_de_texto = []
def crear_texto_simple():
  # "D:\\storage\texto_simple.txt"
  #crear  "x" - Create   "a" - Append   "w" escribir
  file = open(file_name, "w")
  file.write("linea 1 y al mismi tiempo se sobre escribio a lo anterior")
  file.close()

def leer_texto_simple():
  file = open(file_name, "r")  # r+   significa lectura y escritura    rt
  print("esta escrito:", file.read())  # read(3)  leer hsta el caracter 3
  #lista_de_texto = list(file.readline())  # se convierte aformato lista
  #file.seek(0)  # posicionarse el puntero en la pocicion 0 para  leer o escribir
  #print(lista_de_texto)
  file.close()

def add_line_texto_simple(text_add=""):
  file = open(file_name, "a")
  #file.seek(puntero)
  #lista_de_texto = ["sadf", "sadf"]
  file.writelines("\n" + text_add)
  #file.writelines(lista_de_texto)   escribir una variable lista
  file.close()

def add_texto_simple(text_add = "", puntero = 0):
  file = open(file_name, "a")
  file.seek(puntero)
  file.write(text_add)
  file.writelines(lista_de_texto)#escribir una variable lista
  file.close()

def borrar_texto_simple():
  file = open(file_name, "w")
  file.write("")
  file.close()
