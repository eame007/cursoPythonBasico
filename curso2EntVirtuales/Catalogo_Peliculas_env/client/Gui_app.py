import tkinter as tk

def barra_menu(ventana):
    barra_menu = tk.Menu(ventana)
    ventana.config(menu = barra_menu)
    
    menu_inicio = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label="Inicio", menu= menu_inicio)
    menu_inicio.add_command(label="Crear Registro en BD")
    menu_inicio.add_command(label="Eliminar Registro en BD")
    menu_inicio.add_command(label="Salir", command= ventana.destroy)
    
class Frame(tk.Frame):
    
    def __init__(self, ventana = None):
        super().__init__(ventana, width=500 , height=440, background="green")
        self.ventana = ventana
        self.pack()
        self.campos_pelicula()
        
    def campos_pelicula(self):
        self.label_nombre= tk.Label(self, text="Nombre: ")
        self.label_nombre.grid(row=0, column=0)

    