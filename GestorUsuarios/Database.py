import csv
import config
import sys

class Cliente:
    
    def __init__(self, dui, nombre, apellido):
        self.dui = dui
        self.nombre = nombre
        self.apellido = apellido
        
    def __str__(self) -> str:
        return f"({self.dui}) {self.nombre} {self.apellido}"
    

class Clientes:
   
    lista = []

    with open( config.DATABASE_PATH, newline="\n") as fichero:
        reader = csv.reader(fichero, delimiter=";")
        for dui, nombre, apellido in reader:
            cliente = Cliente(dui, nombre, apellido)
            lista.append(cliente) 
    
    @staticmethod
    def BuscarCliente(dui):
        for cliente in Clientes.lista:
            if cliente.dui == dui:
                return cliente
    
    @staticmethod
    def crearCliente(dui, nombre, apellido):
        cliente = Cliente(dui, nombre, apellido)
        Clientes.lista.append(cliente)
        Clientes.guardar()
        return cliente
    
    @staticmethod
    def Modificar(dui, nombre, apellido):
        for indice, cliente in enumerate(Clientes.lista):
            if cliente.dui == dui:
                Clientes.lista[indice].nombre = nombre
                Clientes.lista[indice].apellido = apellido
                Clientes.guardar()
                return Clientes.lista[indice]
    
    @staticmethod
    def Eliminar(dui):
        for indice, cliente in enumerate(Clientes.lista):
            if cliente.dui == dui:
                cliente = Clientes.lista.pop(indice)  
                Clientes.guardar()
                return cliente
    
    @staticmethod
    def guardar():
        with open(config.DATABASE_PATH, "w", newline="\n") as fichero:
            writer = csv.writer(fichero, delimiter=";")
            for cliente in Clientes.lista:
                writer.writerow((cliente.dui, cliente.nombre, cliente.apellido))
        fichero.close()
    