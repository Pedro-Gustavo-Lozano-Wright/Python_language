from tkinter import *
from datetime import datetime
import gs
#import rotatescreen
import RPi.GPIO as gpio
import time
#import RIP.GPIO as GPIO
from datetime import timedelta
import time

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(12, gpio.OUT)

gpio.setup(10, gpio.IN, pull_up_down=gpio.PUD_DOWN)
gpio.setup(16, gpio.IN, pull_up_down=gpio.PUD_DOWN)
gpio.setup(18, gpio.IN, pull_up_down=gpio.PUD_DOWN)
gpio.setup(22, gpio.IN, pull_up_down=gpio.PUD_DOWN)


# time.sleep(0.5)

gs.date_reference = datetime.now()


def clickPlay(): # eventos
    print(str(gs.globalState))
    if str(gs.globalState) == "stop":
        gs.globalState = "play"
        gs.date_reference = datetime.now()
    elif gs.globalState == "play":
        gs.globalState = "stop"
        gs.segundos_inicio = gs.segundos_inicio + gs.segundos_acomulados
        gs.segundos_acomulados = 0
    elif gs.globalState == "fin":
        gs.segundos_acomulados = 0
        gs.segundos_inicio = 0
        gs.segundos_last = 0
        gs.set_point_seg = 0
        gs.set_point_min = 12
        gs.globalState = "stop"
#         window.button.configure(text="play")
    print(str(gs.globalState))


def clickReset():  # evento reset
        gs.segundos_acomulados = 0
        gs.segundos_inicio = 0
        gs.segundos_last = 0
        gs.set_point_seg = 0
        gs.set_point_min = 12
        if gs.globalState == "play":
            gs.globalState = "stop"
            #window.button.configure(text="play")

def masTiempo():  # evento reset
    if gs.set_point_min < 60:
        gs.set_point_min = gs.set_point_min + 1

def menosTiempo():  # evento reset
    if gs.set_point_min > 1:
        gs.set_point_min = gs.set_point_min - 1


def formato(segundos): # segundos_a_segundos_minutos_y_horas
    horas = int(segundos/60/60)
    segundos -= horas*60*60
    minutos = int(segundos/60)
    segundos -= minutos*60
    return f"{minutos:02d}:{segundos:02d}"

def mainCode(): # estados
    # print(gs.globalState)
    tempo_set_point = (gs.set_point_min * 60) + gs.set_point_seg
    if gpio.input(10)==gpio.HIGH:
        print('play/stop')
        gpio.output(12, False)
        time.sleep(0.5)
        clickPlay()
    elif gpio.input(16)==gpio.HIGH:
        print('reset')
        gpio.output(12, False)
        time.sleep(0.5)
        clickReset()
    elif gpio.input(18)==gpio.HIGH:
        print('mas un minuto')
        gpio.output(12, False)
        time.sleep(0.5)
        masTiempo()
    elif gpio.input(22)==gpio.HIGH:
        print('menos un minuto')
        gpio.output(12, False)
        time.sleep(0.5)
        menosTiempo()
    

    if gs.globalState == "stop":
        pass
#         window.button.configure(text="play")
    if gs.globalState == "play":
#         window.button.configure(text="stop")
        gs.segundos_acomulados = (datetime.now() - gs.date_reference).total_seconds()
        
        if (int(tempo_set_point - gs.segundos_acomulados - gs.segundos_inicio) == 0):
            gpio.output(12, True)
            print('chicharra!!!!')
            
        if (int(tempo_set_point - gs.segundos_acomulados - gs.segundos_inicio) < 0):
            gpio.output(12, True)
            print('chicharra!!!!')
            gs.globalState = "stop"
            tempo_set_point = 0
            gs.segundos_acomulados = 0
            gs.segundos_inicio = 0
            gs.segundos_last = 0
            gs.set_point_seg = 0
            gs.set_point_min = 0
            time.sleep(3) # duracion de chicharra
            gpio.output(12, False)
            print('chicharra apagada')
            gs.globalState = "fin"
#             window.button.configure(text="reset")
    time_show = tempo_set_point - gs.segundos_acomulados - gs.segundos_inicio 
    if (time_show > 0):
        tempralizador.set(formato(int(time_show)))


def whileCode():
    mainCode()
    window.after(100, whileCode)  # INTERVALO DE REFRESCO EN milisegundos

window = Tk()
window.attributes('-fullscreen', True)
#window.geometry('350x200')

window.configure(bg='black')
window.title("PALENQUE EL GAYO DE ORO")
tempralizador = StringVar(window, value='00:00')

# window.button = Button(window, text="play", command=clickPlay, fg="red", bg="black")
# window.button.pack(side="top")

# Bodoni MT Black, Broadway, Copperplate Gothic Bold,Engravers MT, Rockwell Extra Bold
window.etiqueta = Label(
    window,
    textvariable=tempralizador,
    font=("Broadway", 380,),
    fg="red", bg="black")
window.etiqueta.place(relx=0.5, rely=0.5, anchor=CENTER)

# window.buttonQuit = Button(window, text="funcion", command=clickReset, fg="red", bg="black")#window.destroy)
# window.buttonQuit.pack(side="bottom")

#rotate_screen = rotatescreen.get_primary_display()
#rotate_screen.set_landscape_flipped()
app = Frame()
whileCode()
app.pack()
app.mainloop()