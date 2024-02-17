from tkinter import *
from tkinter import ttk
import Database as db
from tkinter.messagebox import askokcancel, WARNING
import Helpers
from functools import partial



#Comentario de prueba
class CenterWidgetMixin:
    def center(self,):
        self.update()
        w = self.winfo_width()
        h = self.winfo_height()
        ws = self.winfo_screenwidth()
        hs = self.winfo_screenheight()
        x = int((ws/2) - (w/2))
        y = int((hs/2) - (h/2))
        self.geometry(f"{w}x{h}+{x}+{y}")
        
class CreateClientWindows(Toplevel, CenterWidgetMixin):
    def __init__(self, padre):
        super().__init__(padre)
        self.validaciones = [False, False, False]
        self.title("Crear Cliente")
        self.build()
        self.center()
        #Las dos sentencias siguientes nos eivitasn regresar a la principal hasta cerrar las emergentes
        self.transient(padre)
        self.grab_set()
    
    def crear_cliente(self):
        self.master.treeview.insert(
               parent="",index="end", iid=self.dui,
               values=(self.dui.get(), self.nombre.get(), self.apellido.get()))
        self.close()
           
    
    def build(self):
        frame = Frame(self)
        frame.pack(padx=20, pady=10)
        Label(frame, text="DUI").grid(row=0, column=0)
        Label(frame, text="Nombres").grid(row=0, column=1)
        Label(frame, text="Apellidos").grid(row=0, column=2)

        dui = Entry(frame)
        dui.grid(row=1, column=0)
        dui.bind("<KeyRelease>", lambda event: self.validate(event,0))
        nombres = Entry(frame)
        nombres.grid(row=1, column=1)
        nombres.bind("<KeyRelease>", lambda event: self.validate(event,1))
        apellidos = Entry(frame)
        apellidos.grid(row=1, column=2)
        apellidos.bind("<KeyRelease>", lambda event: self.validate(event,2))

        
        frame2 = Frame(self)
        frame2.pack(pady=10)
        self.btncrear = Button(frame2, text="Crear", command=self.crear_cliente, state=DISABLED)
        self.btncrear.grid(row=0, column=0)
        Button(frame2, text="Cancelar", command=self.close).grid(row=0, column=1)
        
        self.dui = dui
        self.apellido =apellidos
        self.nombre = nombres
        
   
    def validate(self, event, indice):
        valor = event.widget.get()
        valido = Helpers.validar_dui(valor, db.Clientes.lista) if indice == 0 else (valor.isalpha() and len(valor)>=2 and len(valor)<=30)
        event.widget.configure(bg="Green") if valido else event.widget.configure(bg="Red")
        #Cambiando estado de boton
        self.validaciones[indice] = valido
        print(self.validaciones)
        if self.validaciones == [True, True, True]:
            self.btncrear.config(state=NORMAL)


    def close(self):
        #Destruye la subventada y actualzia el frame
        self.destroy()
        self.update()
      
class EditClienteWindows(Toplevel, CenterWidgetMixin):
    def __init__(self, padre):
        super().__init__(padre)
        self.validaciones = [True, True]
        self.title("Editar Cliente")
        self.build()
        self.center()
        self.transient(padre)
        self.grab_set()
    
    def editar_cliente(self):
        pass           
    
    def build(self):
        frame = Frame(self)
        frame.pack(padx=20, pady=10)
        Label(frame, text="DUI(No Editable)").grid(row=0, column=0)
        Label(frame, text="Nombres").grid(row=0, column=1)
        Label(frame, text="Apellidos").grid(row=0, column=2)

        dui = Entry(frame)
        dui.grid(row=1, column=0)
        nombres = Entry(frame)
        nombres.grid(row=1, column=1)
        nombres.bind("<KeyRelease>", lambda event: self.validate(event,0))
        apellidos = Entry(frame)
        apellidos.grid(row=1, column=2)
        apellidos.bind("<KeyRelease>", lambda event: self.validate(event,1))

        
        frame2 = Frame(self)
        frame2.pack(pady=10)
        self.btncrear = Button(frame2, text="Modificar", command=self.editar_cliente)
        self.btncrear.grid(row=0, column=0)
        Button(frame2, text="Cancelar", command=self.close).grid(row=0, column=1)
        
        self.dui = dui
        self.apellido =apellidos
        self.nombre = nombres
        
        cliente = self.master.treeview.focus()
        campos = self.master.treeview.item(cliente, "values")
        dui.insert(0, campos[0])
        dui.config(state= DISABLED)
        nombres.insert(0, campos[1])
        apellidos.insert(0, campos[2])
   
    def validate(self, event, indice):
        valor = event.widget.get()
        valido = (valor.isalpha() and len(valor)>=2 and len(valor)<=30)
        event.widget.configure(bg="Green") if valido else event.widget.configure(bg="Red")
        self.validaciones[indice] = valido
        print(self.validaciones)
        if self.validaciones != [True, True]:
            self.btncrear.config(state=DISABLED)


    def close(self):
        #Destruye la subventada y actualzia el frame
        self.destroy()
        self.update()
            
        
class MainWindow(Tk, CenterWidgetMixin): # edited
   
    def __init__(self):
        super().__init__()
        self.title('Gestor de clientes')
        self.Build()
        self.center() # new

    def Build(self):
       frame = Frame(self)
       frame.pack()
       treeview = ttk.Treeview(frame)
       self.treeview = treeview
       treeview["columns"] = ('DUI', 'Nombre', 'Apellido')

        #CONFIGURACION DE COLUMNAS
       treeview.column("#0", width=0, stretch=NO)
       treeview.column('DUI', anchor=CENTER)
       treeview.column("Nombre", anchor=CENTER)
       treeview.column("Apellido", anchor=CENTER)
    
        #Configuramos las cabeceras de la tabla
       treeview.heading("DUI", text="DUI", anchor=CENTER)
       treeview.heading("Nombre", text="Nombre", anchor=CENTER)
       treeview.heading("Apellido", text="Apellido", anchor=CENTER)
       
       #Agregamos scroollbar
       scrolbar = Scrollbar(frame)
       scrolbar.pack(side=RIGHT, fill=Y)   
       treeview['yscrollcommand'] =scrolbar.set


       for cliente in db.Clientes.lista:
           treeview.insert(
               parent="",index="end", iid=cliente.dui,
               values=(cliente.dui, cliente.nombre, cliente.apellido)
           )

       treeview.pack()
       
       frame = Frame(self)
       frame.pack(pady=20)
       Button(frame, text="Crear", command=self.Crear).grid(row=0, column=0)
       Button(frame, text="Modificar", command=self.Editar).grid(row=0, column=1)
       Button(frame, text="Borrar", command=self.Borrar).grid(row=0, column=2)

       

    def Borrar(self):
        cliente = self.treeview.focus()
        if cliente:
            campos = self.treeview.item(cliente, "values")
            confitmar = askokcancel(
                title="Borrado",
                message= f"¿Borrar a {campos[1]} {campos[2]}",
                icon = WARNING
            )
            
    
    def Crear(self):
        CreateClientWindows(self)
    
    def Editar(self):
        if self.treeview.focus():
            EditClienteWindows(self)

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()  
