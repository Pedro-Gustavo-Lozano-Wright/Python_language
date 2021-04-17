from __future__ import annotations
from abc import abstractmethod

def state():

    class Context:
        _state = None

        def __init__(self, state: State) -> None:
            self.transition_to(state)

        def transition_to(self, state: State):
            print(f"Cambiando a {type(state).__name__}")  # logica de cambio
            self._state = state
            self._state.context = self

        def request1(self):
            self._state.handle1()  # logica de cambio

        def request2(self):
            self._state.handle2()  # logica de cambio

    class State():

        @property
        def context(self) -> Context:
            return self._context

        @context.setter
        def context(self, context: Context) -> None:
            self._context = context

        @abstractmethod
        def handle1(self) -> None:
            pass

        @abstractmethod
        def handle2(self) -> None:
            pass

    class Estado_A(State):
        def handle1(self) -> None:  # A estado 1
            print("A1 a B2")
            self.context.transition_to(Estado_B())  # logica de cambio

        def handle2(self) -> None:  # A estado 2
            print("A1 a A2")

    class Estado_B(State):
        def handle1(self) -> None:  # B estado 1
            print("B2 a B1")

        def handle2(self) -> None:  # B estado 2
            print("B2 a A1")
            self.context.transition_to(Estado_A())  # logica de cambio

    context = Context(Estado_A())
    print("-")  # A estado 1
    context.request1()
    print("-")  # B estado 1
    context.request2()
    print("-")  # A estado 2
    context.request2()
    print("-")  # B estado 2
    context.request1()
    # A estado 1


