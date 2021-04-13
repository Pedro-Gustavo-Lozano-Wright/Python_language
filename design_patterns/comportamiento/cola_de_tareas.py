
import abc

def cola_de_tareas():

    class guardar_y_ejecutar:

        def __init__(self):
            self._commands = []

        def guardar_tareas(self, command):
            self._commands.append(command)

        def executar_tareas(self):
            for command in self._commands:
                command.execute()

    class Command(metaclass=abc.ABCMeta):

        def __init__(self, receiver):
            self._receiver = receiver

        @abc.abstractmethod
        def execute(self):
            pass

    class Tarea_1(Command):

        def execute(self):
            self._receiver.action()
            print("Tarea1")

    class Tarea_2(Command):

        def execute(self):
            self._receiver.action()
            print("Tarea2")

    class Receiver:

        def action(self):
            print("Receiver")

    receiver = Receiver()
    tarea_1 = Tarea_1(receiver)
    tarea_2 = Tarea_2(receiver)
    lista_de_tareas = guardar_y_ejecutar()
    lista_de_tareas.guardar_tareas(tarea_1)
    lista_de_tareas.guardar_tareas(tarea_2)
    lista_de_tareas.executar_tareas()



