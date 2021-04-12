
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

  # crear carpeta
  # os.listdir()
  # os.mkdir('test/folder_name')

  # extraer ruta actual
  # print(os.getcwdb())

  # r significa solo leer - read
  # a añadir - Append
  # w escribir - Write
  # x crear - Create, returns an error if the file exists
  # t - Text - Default value. Text mode
  # b - Binary   rb wb en formato no lo legible por otros programas
'''
close()	Closes an opened file. It has no effect if the file is already closed.
detach()	Separates the underlying binary buffer from the TextIOBase and returns it.
fileno()	Returns an integer number (file descriptor) of the file.
flush()	Flushes the write buffer of the file stream.
isatty()	Returns True if the file stream is interactive.
read(n)	Reads at most n characters from the file. Reads till end of file if it is negative or None.
readable()	Returns True if the file stream can be read from.
readline(n=-1)	Reads and returns one line from the file. Reads in at most n bytes if specified.
readlines(n=-1)	Reads and returns a list of lines from the file. Reads in at most n bytes/characters if specified.
seek(offset,from=SEEK_SET)	Changes the file position to offset bytes, in reference to from (start, current, end).
seekable()	Returns True if the file stream supports random access.
tell()	Returns the current file location.
truncate(size=None)	Resizes the file stream to size bytes. If size is not specified, resizes to current location.
writable()	Returns True if the file stream can be written to.
write(s)	Writes the string s to the file and returns the number of characters written.
writelines(lines)	Writes a list of lines to the file.   

Conocer el directorio actual	 os.getcwd()
Cambiar de directorio de trabajo os.chdir(nuevo_path)
ir al directorio de trabajo raíz os.chroot()
Crear un directorio	             os.mkdir(path[, modo])
Crear directorios recursivamente os.mkdirs(path[, modo])
Eliminar un archivo	             os.remove(path)
Eliminar un directorio	         os.rmdir(path)
Eliminar directorios recursivos	 os.removedirs(path)
Renombrar un archivo       	     os.rename(actual, nuevo)
Crear un enlace simbólico	     os.symlink(path, nombre_destino)


Ruta absoluta	                 os.path.abspath(path)
Directorio base	                 os.path.basename(path)
si un directorio existe	         os.path.exists(path)
Conocer tamaño del directorio	 os.path.getsize(path)
Saber si una ruta es un archivo	 os.path.isfile(path)
si es un directorio	             os.path.isdir(path)
si es un enlace simbólico	     os.path.islink(path)

'''



