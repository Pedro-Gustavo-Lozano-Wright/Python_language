from __future__ import annotations
from abc import ABC, abstractmethod

def factori_metod():
    class Creator():

        @abstractmethod
        def factory_method(self):
            pass

        def some_operation(self) -> str:
            product = self.factory_method()

            result = f"Creator: {product.operation()}"

            return result

    class ConcreteCreator1(Creator):

        def factory_method(self) -> Product:
            print("-samsun tab-")
            return ConcreteProduct1()

    class ConcreteCreator2(Creator):
        def factory_method(self) -> Product:
            print("-samsun cel-")
            return ConcreteProduct2()

    class Product():
        @abstractmethod
        def operation(self) -> str:
            pass

    class ConcreteProduct1(Product):
        def operation(self) -> str:
            return "{Product1 - tab}"

    class ConcreteProduct2(Product):
        def operation(self) -> str:
            return "{Product2 - cel}"

    def client_code(creator: Creator) -> None:
        print(f"Client: {creator.some_operation()}", end="")

    print("Creator1.")
    client_code(ConcreteCreator1())

    print("\n")

    print("Creator2.")
    client_code(ConcreteCreator2())
