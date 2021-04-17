
from __future__ import annotations
from abc import abstractmethod
from typing import List

def observer_subscripcion():

    class Subject():

        @abstractmethod
        def attach(self, observer: Observer) -> None:
            pass

        @abstractmethod
        def detach(self, observer: Observer) -> None:
            pass

        @abstractmethod
        def notify(self) -> None:
            pass

    class Lista_de_suscripcion(Subject):

        _state: int = None

        _observers: List[Observer] = []

        def attach(self, observer: Observer) -> None:
            print("Suscrito")
            self._observers.append(observer)

        def detach(self, observer: Observer) -> None:
            print("Dsuscrito")
            self._observers.remove(observer)

        def notify(self) -> None:
            print("Enviar notificaciones...")
            for observer in self._observers:
                observer.update(self)

        def some_business_logic(self) -> None:
            print("\se puede mejorar las cracteristicas "
                  "de los usuarios y la logica para a "
                  "que clase de usuario se le envia")
            self._state = 0

            print(f"Envio random  {self._state}")
            self.notify()

    class Observer():

        @abstractmethod
        def update(self, subject: Subject) -> None:
            pass

    class ConcreteObserverA(Observer):
        def update(self, subject: Subject) -> None:
            if subject._state == 0:
                print("Usuario A")

    class ConcreteObserverB(Observer):
        def update(self, subject: Subject) -> None:
            if subject._state == 0 or subject._state >= 2:
                print("Usuario B")

    class ConcreteObserverC(Observer):
        def update(self, subject: Subject) -> None:
            if subject._state == 0 or subject._state >= 2:
                print("Usuario C")

    if __name__ == "__main__":
        # The client code.

        subject = Lista_de_suscripcion()

        observer_a = ConcreteObserverA()
        subject.attach(observer_a)

        observer_b = ConcreteObserverB()
        subject.attach(observer_b)

        observer_c = ConcreteObserverC()
        subject.attach(observer_c)

        subject.some_business_logic()

        subject.detach(observer_c)

        subject.some_business_logic()

        subject.detach(observer_a)

        subject.some_business_logic()