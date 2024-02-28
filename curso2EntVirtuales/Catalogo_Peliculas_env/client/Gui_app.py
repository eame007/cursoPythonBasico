import tkinter as tk

def barra_menu(ventana):
    barra_menu = tk.Menu(ventana)
    ventana.config(menu = barra_menu)

class Frame(tk.Frame):
    
    def __init__(self, ventana = None):
        super().__init__(ventana, width=500 , height=440, background="green")
        self.ventana = ventana
        self.pack()

    