from tkinter import *
from tkinter import filedialog
from io import open

ruta = ""

def nuevo():
    global ruta
    mensaje.set("Nuevo Fichero")
    ruta = ""
    areaTexto.delete(1.0,"end")
    raiz.title("Pando")
    
def abrir():
    global ruta
    ruta = filedialog.askopenfilename(initialdir=".", filetypes=(("Dicheros de texto","*.txt"),),title="Abrir un fichero de texto")
    if ruta != "":
        fichero = open(ruta, "r")
        contenido = fichero.read()
        areaTexto.delete(1.0, "end")
        areaTexto.insert("insert", contenido)
        fichero.close()
        raiz.title(ruta + "-Pando")
def guardar():
    mensaje.set("Guardando Fichero")
    if ruta != "":
        contenido = areaTexto.get(1.0,"end-1c")
        fichero = open(ruta, "w+")
        fichero.write(contenido)
        fichero.close()
        mensaje.set("Fichero guardado con exito")
    else:
        guardarComo()


def guardarComo():
    mensaje.set("Guardando Fichero")
    global ruta
    fichero = filedialog.asksaveasfile(title="Guardar Fichero Como", mode="w", defaultextension=".txt")
    if fichero is not NONE:
        ruta  = fichero.name
        contenido = areaTexto.get(1.0,"end-1c")
        fichero = open(ruta, "w+")
        fichero.write(contenido)
        fichero.close()
        mensaje.set("Fichero guardado con exito")
   

raiz = Tk()
raiz.title("Pando")

barramenu = Menu(raiz)

filemenu = Menu(barramenu, tearoff=0)
filemenu.add_command(label = "Nuevo", command=nuevo)
filemenu.add_command(label = "Abrir", command=abrir)
filemenu.add_command(label = "Guardar", command=guardar)
filemenu.add_command(label = "Guardar Como", command=guardarComo)
filemenu.add_separator()
filemenu.add_command(label = "Salir", command=raiz.quit)
barramenu.add_cascade(menu = filemenu, label="Archivo")


#Caja de tecto
areaTexto = Text()
areaTexto.pack(fill=BOTH, expand=1)
areaTexto.config(bd=0, padx=6, pady=4, font=("NotoSans",11))

#Monitor INferior
mensaje = StringVar()
mensaje.set("Bienvenido al editor pando")
monitor = Label(raiz,textvariable=mensaje, justify=LEFT)
monitor.pack(side=LEFT)

raiz.config(menu=barramenu)


raiz.mainloop()