from __future__ import annotations
from abc import abstractmethod
from typing import List

def ejemplo_composite():
    class Componente():  # el componente se puede convertir en caja u objeto

        """
        el componente se puede convertir en caja u objeto,
        tiene la propiedad de contener un objeto de su
        propia clase
        """

        @property
        def parent(self) -> Componente:
            return self._parent

        @parent.setter
        def parent(self, parent: Componente):
            self._parent = parent

        def add(self, component: Componente) -> None:
            pass

        def remove(self, component: Componente) -> None:
            pass

        def is_composite(self) -> bool:
            return False

        @abstractmethod
        def operation(self) -> str:
            pass

    class objeto_final_de_rama(Componente):

        def operation(self) -> str:
            return "objeto"

    class caja_contenedor(Componente):

        def __init__(self) -> None:
            self._children: List[Componente] = []

        def add(self, component: Componente) -> None:
            self._children.append(component)
            component.parent = self

        def remove(self, component: Componente) -> None:
            self._children.remove(component)
            component.parent = None

        def is_composite(self) -> bool:
            return True

        def operation(self) -> str:
            results = []
            for child in self._children:
                results.append(child.operation())
            return f"caja({'+'.join(results)})"

    def client_code(component: Componente) -> None:

        print(f"{component.operation()}", end="")

    def client_code2(component1: Componente, component2: Componente) -> None:

        if component1.is_composite():
            component1.add(component2)

        print(f"{component1.operation()}", end="")

    simple = objeto_final_de_rama()

    print(" el componente se puede convertir "
          "en caja u objeto, tiene la propiedad "
          "de contener un objeto de su propia clase")

    print("\n")
    print("este es un componente simple"
          " y va al final de las ramas")
    client_code(simple)
    print("\n")

    print("este es una rama simple")
    tronco_simple = caja_contenedor()
    tronco_simple.add(simple)
    client_code(tronco_simple)
    print("\n")

    # ...as well as the complex composites.
    tronco_del_arbol = caja_contenedor()

    rama_1 = caja_contenedor()
    rama_1.add(objeto_final_de_rama())
    rama_1.add(objeto_final_de_rama())

    rama_2 = caja_contenedor()
    rama_2.add(objeto_final_de_rama())

    tronco_del_arbol.add(rama_1)
    tronco_del_arbol.add(rama_2)

    print("este es un arbol con ramas")
    client_code(tronco_del_arbol)
    print("\n")

    print("de esta manera se rvisan todos "
          "los elementos en automatico")
    client_code2(tronco_del_arbol, simple)
