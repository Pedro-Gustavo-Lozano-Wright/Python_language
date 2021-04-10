from tkinter import *

def funcion_grafica():
    window = Tk()
    window.title("Titulo")

    window.geometry('350x200')

    lbl = Label(window, text="Texto", font=("Arial Bold", 12,))
    lbl.grid(column=2, row=0)

    def clicked():
        lbl.configure(text="Hola mundo en python!!")

    btn = Button(window, text="Click Me", command=clicked)
    btn.grid(column=3, row=0)

    window.mainloop()
