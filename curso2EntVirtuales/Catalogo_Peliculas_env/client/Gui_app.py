import tkinter as tk

class Frame(tk.Frame):
    
    def __init__(self, ventana = None):
        super().__init__(ventana, width=500 , height=440, background="green")
        self.ventana = ventana
        self.pack()

    