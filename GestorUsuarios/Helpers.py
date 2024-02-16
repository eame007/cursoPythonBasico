import re
import os
import platform

"""Funcion para limpiar la consola"""
def limpiar_Pantalla():
    os.system("cls") if platform.system() == "Windows" else os.system("clear")
    

"""Funcion para leer texto de pantall"""
def leerTexto(longitud_min =0,longitud_max=100, mensaje=None):
    print(mensaje) if mensaje else None
    while True:
        texto = input("> ")
        if len(texto) >= longitud_min and len(texto)<=longitud_max:
            return texto
        else:
            print("Formato invalido")
    
"""Funcion para validar que el DUI tenga un formato valido"""
def validar_dui(dui, lista):
    if not re.match(r'^[0-9]+$', dui) or len(dui)<8:#Aqui podria validar letras con [A-Z] o [a-z] o [A-z]
        print("DUI incorrecto debe cumplir el formato ########")
        return False
    for cliente in lista:
        if cliente.dui == dui:
            print("DUI utilizado por otro cliente.")
            return False
    return True