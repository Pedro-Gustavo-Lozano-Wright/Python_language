from __future__ import annotations
from abc import abstractmethod
from typing import Any, Optional

def cadena_de_operacion():

    class Handler():

        @abstractmethod
        def set_next(self, handler: Handler) -> Handler:
            pass

        @abstractmethod
        def handle(self, request) -> Optional[str]:
            pass

    class AbstractHandler(Handler):

        _next_handler: Handler = None

        def set_next(self, handler: Handler) -> Handler:
            self._next_handler = handler
            # Returning a handler from here will let us link handlers in a
            # convenient way like this:
            # respuesta_1.set_next(respuesta_2).set_next(respuesta_3)
            return handler

        @abstractmethod
        def handle(self, request: Any) -> str:
            if self._next_handler:
                return self._next_handler.handle(request)

            return None

    class respuesta_1_Handler(AbstractHandler):
        def handle(self, request: Any) -> str:
            if request == "Banana":
                return f"respuesta 1: {request}"
            else:
                return super().handle(request)

    class respuesta_2_Handler(AbstractHandler):
        def handle(self, request: Any) -> str:
            if request == "naranja":
                return f"respuesta 2: {request}"
            else:
                return super().handle(request)

    class respuesta_3_Handler(AbstractHandler):
        def handle(self, request: Any) -> str:
            if request == "MeatBall":
                return f"respuesta 3: {request}"
            else:
                return super().handle(request)

    def client_code(handler: Handler) -> None:

        for food in ["naranja", "Banana", "Coffee"]:
            print(f"\nPregunta por {food}?")
            result = handler.handle(food)
            if result:
                print(f"  {result}", end="")
            else:
                print(f" {food} se ignoro", end="")

    respuesta_1 = respuesta_1_Handler()
    respuesta_2 = respuesta_2_Handler()
    respuesta_3 = respuesta_3_Handler()

    respuesta_1.set_next(respuesta_2).set_next(respuesta_3)

    # The client should be able to send a request to any handler, not just the
    # first one in the chain.
    print("se estructura el orden deseado de operacion")
    print("Chain: respuesta_1 > respuesta_2 > respuesta_3")
    client_code(respuesta_1)
    print("\n\n---\n")
    print("se puede seleccionar solo una sub estructura ")
    print("Subchain: respuesta_2 > respuesta_3")

    client_code(respuesta_2)


