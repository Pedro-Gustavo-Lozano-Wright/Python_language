# pip install pynput
from pynput import keyboard as kb
import datetime

memory_out = ["a", "b", "c"]
list_time = [1, 1]  # forzar variable global


def pulsa(tecla):
    print(str(tecla) + ' pulsado')
    list_time[0] = list_time[1]
    list_time[1] = datetime.datetime.now().second
    #
    print(list_time)
    global memory_out  # forzar variable global
    memory_out[0] = memory_out[1]
    memory_out[1] = memory_out[2]
    memory_out[2] = str(tecla)

    if (memory_out[1] == memory_out[2]):
        if(list_time[0] == list_time[1] or list_time[1] == (list_time[0]) + 1):
            if (memory_out[2].islower() or memory_out[2][1].isnumeric()):
                print("Se a repetido una tecla por accidente")

    if (memory_out == ["Key.esc", "Key.esc", "Key.esc"]):
        print("kill")
        return False

def suelta(tecla):
    print(str(tecla) + ' Soltado')
    pass

kb.Listener(pulsa, suelta).run()

