from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import Any, List

def ejemplo_iterador():

    class Iterador(Iterator):

        _position: int = None

        _reverse: bool = False

        def __init__(self, collection: Colleccion_de_objetos, reverse: bool = False) -> None:
            self._collection = collection
            self._reverse = reverse
            self._position = -1 if reverse else 0

        def __next__(self):
            try:
                value = self._collection[self._position]
                self._position += -1 if self._reverse else 1
            except IndexError:
                raise StopIteration()

            return value

    class Colleccion_de_objetos(Iterable):

        def __init__(self, collection: List[Any] = []) -> None:
            self._collection = collection

        def __iter__(self) -> Iterador:
            return Iterador(self._collection)

        def get_reverse_iterator(self) -> Iterador:
            return Iterador(self._collection, True)

        def add_item(self, item: Any):
            self._collection.append(item)

    # The client code may or may not know about the Concrete Iterator or
    # Collection classes, depending on the level of indirection you want to keep
    # in your program.

    collection = Colleccion_de_objetos()
    collection.add_item("1ro")
    collection.add_item("2do")
    collection.add_item("3ro")
    collection.add_item("4do")
    collection.add_item("5ro")
    collection.add_item("6do")
    collection.add_item("7ro")

    print("atravezar derechp:")
    print("\n".join(collection))
    print("")

    print("atravezar en reversa:")
    print("\n".join(collection.get_reverse_iterator()), end="3ro")

