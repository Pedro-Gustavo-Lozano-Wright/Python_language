from __future__ import annotations
from abc import abstractmethod
from typing import List

def strategy():

    class Context():

        def __init__(self, strategy: Strategy) -> None:
            self._strategy = strategy

        @property
        def strategy(self) -> Strategy:
            return self._strategy

        @strategy.setter
        def strategy(self, strategy: Strategy) -> None:
            self._strategy = strategy

        def do_some_business_logic(self) -> None:
            print("en estta clase se usa la vaariable strategy asignada desde afuera")
            result = self._strategy.do_algorithm(["a", "b", "c", "d", "e"])
            print(",".join(result))
            print("el algoritmo o estrateguia seleccionada se asiggna a la variable")

    class Strategy():

        @abstractmethod
        def do_algorithm(self, data: List):
            pass

    class ConcreteStrategyA(Strategy):
        def do_algorithm(self, data: List) -> List:
            # se establece el algoritmo que se puede asignar a un "contexto"
            return sorted(data)

    class ConcreteStrategyB(Strategy):
        def do_algorithm(self, data: List) -> List:
            # se establece el algoritmo que se puede asignar a un "contexto"
            return reversed(sorted(data))

    context = Context(ConcreteStrategyA())
    print("Client: Strategy is set to normal sorting.")
    context.do_some_business_logic()
    print()

    print("Client: Strategy is set to reverse sorting.")
    context.strategy = ConcreteStrategyB()
    context.do_some_business_logic()
