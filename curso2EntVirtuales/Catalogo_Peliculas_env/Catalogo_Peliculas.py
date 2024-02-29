import tkinter as tk
from  client.Gui_app import  Frame, barra_menu

def main():# Crear la ventana
    ventana = tk.Tk()
    ventana.title("Catalogo de peliculas")

    # Establecer el icono
    icono = tk.PhotoImage(file="image/spotify.png")  # Reemplaza "icono.png" con la ubicación y nombre de tu imagen
    ventana.iconphoto(True, icono)
    ventana.resizable(1,1)
    app = Frame(ventana = ventana)
    barra_menu(ventana)
    app.mainloop() 

if __name__ == '__main__':
    main()