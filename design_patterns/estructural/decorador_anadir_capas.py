

def decorador_anadir_capas():
    class Component():

        def operation(self) -> str:
            return "operacion"

    class Objeto_Component(Component):

        def operation(self) -> str:
            return "objeto"

    class Decorator(Component):
        _component: Component = None

        def __init__(self, component: Component) -> None:
            self._component = component

        @property
        def component(self) -> str:
            return self._component

        def operation(self) -> str:
            return self._component.operation()

    class capa_a(Decorator):

        def operation(self) -> str:
            return f"capa_A({self.component.operation()})"

    class capa_B(Decorator):

        def operation(self) -> str:
            return f"capa_B({self.component.operation()})"

    def mostrar_arbol(component: Component) -> None:
        print(f"RESULT: {component.operation()}", end="")



    if __name__ == "__main__":
        # This way the client code can support both simple components...
        objeto = Objeto_Component()
        print("Objeto simple:")
        mostrar_arbol(objeto)
        print("\n")
        # ...as well as decorated ones.
        #
        # Note how decorators can wrap not only simple components but the other
        # decorators as well.
        capa_a = capa_a(objeto)
        capa_b = capa_B(capa_a)
        print("Arbol de objetos:")
        mostrar_arbol(capa_b)

