import pickle


class guardar_objetos_en_archivo():
    lista_de_objetos = []
    def __init__(self):
        archivo_lisa_de_objetos = open("archivo", "ab+")  # un archivo binario permite guardar clases
        archivo_lisa_de_objetos.seek(0)
        try:
            self.lista_de_objetos = pickle.load(archivo_lisa_de_objetos)
        except:
            print("no hay nada")
        finally:
            archivo_lisa_de_objetos.close()
            del (archivo_lisa_de_objetos)

    def agregar_objetos(self, objeto):
        self.lista_de_objetos.append(objeto)
        self.guardar_lista_en_archivo()

    def mostrar_lista(self):
        for obj in self.lista_de_objetos:
            obj.preguntar_nombre()

    def guardar_lista_en_archivo(self):
        archivo_de_objetos = open("archivo", "wb")
        pickle.dump(self.lista_de_objetos, archivo_de_objetos)  # guardar
        archivo_de_objetos.close()
        del (archivo_de_objetos)

#r significa solo leer - read
#a añadir - Append
#w escribir - Write
#x crear - Create, returns an error if the file exists
#t - Text - Default value. Text mode
#b - Binary   rb wb en formato no lo legible por otros programas
