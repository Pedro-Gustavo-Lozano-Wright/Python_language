'''
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
            print(obj)

    def guardar_lista_en_archivo(self):
        archivo_lisa_de_objetos = open("demofile4.txt", "wb")
        pickle.dump(self.lista_de_objetos, archivo_lisa_de_objetos)  # guardar
        archivo_lisa_de_objetos.close()
        del (archivo_lisa_de_objetos)
'''