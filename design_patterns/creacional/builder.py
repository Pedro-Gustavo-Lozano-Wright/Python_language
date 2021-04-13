from __future__ import annotations
from abc import abstractmethod, abstractproperty
from typing import Any

def ejemplo_builder():

    class Builder():  # se crean las llamadas a los
        # metodos complementarios

        @abstractproperty
        def product(self) -> None:
            print("product")

        @abstractmethod
        def metodo_caracteristica_a(self) -> None:
            print("metodo_caracteristica_a")

        @abstractmethod
        def metodo_caracteristica_b(self) -> None:
            print("metodo_caracteristica_b")

        @abstractmethod
        def metodo_caracteristica_c(self) -> None:
            print("metodo_caracteristica_c")

    class ConcreteBuilder(Builder):  # puede haber Builder1, Builder2

        def __init__(self) -> None:
            self.reset()  # ------ considerar borrar si afecta funcionamiento

        def reset(self) -> None:
            self._product = Product()  # ------ considerar borrar si afecta funcionamiento

        @property
        def product(self) -> Product:
            product = self._product
            self.reset()
            return product

        def metodo_caracteristica_a(self) -> None:
            self._product.add("-A-")

        def metodo_caracteristica_b(self) -> None:
            self._product.add("-B-")

        def metodo_caracteristica_c(self) -> None:
            self._product.add("-C-")

    class Product():

        def __init__(self) -> None:
            self.parts = []

        def add(self, part: Any) -> None:
            self.parts.append(part)

        def list_parts(self) -> None:
            print(f"Product parts: {', '.join(self.parts)}", end="")

    class Director:

        def __init__(self) -> None:
            self._builder = None

        @property
        def builder(self) -> Builder:
            return self._builder

        @builder.setter
        def builder(self, builder: Builder) -> None:
            self._builder = builder

        def build_minimal_viable_product(self) -> None:
            self.builder.metodo_caracteristica_a()

        def build_full_featured_product(self) -> None:
            self.builder.metodo_caracteristica_a()
            self.builder.metodo_caracteristica_b()
            self.builder.metodo_caracteristica_c()

    if __name__ == "__main__":
        director = Director()
        builder = ConcreteBuilder()
        director.builder = builder

        print("Standard basic product: ")
        director.build_minimal_viable_product()
        builder.product.list_parts()

        print("\n")

        print("Standard full featured product: ")
        director.build_full_featured_product()
        builder.product.list_parts()

        print("\n")

        # Remember, the Builder pattern can be used without a Director class.
        print("Custom product: ")
        builder.metodo_caracteristica_a()
        builder.metodo_caracteristica_b()
        builder.product.list_parts()



