from time import sleep
from threading import Thread
import os
from queue import Queue

#Definicion de variables globales
 #R Estado del servidor
 #mc: Master Clock
#Tiempo en el que la maquina se arruinara
#CLK_1 = 1 , CLK_2 = 4 , CLK_3 = 9 
#Criterio para las siguientes fallas
#MC +10
#Tiempo que el  server demora en reparar  la maquina
#CLK_Reparacion = MC + 5
#Numero de clientes en sistema n = 0
fila = {
    'paso':0,
    'mc': 0,
    'clk_1': 1,
    'clk_2': 4,
    'clk_3': 9,
    'clk_reparacion': 0,
    'n': 0,
    'r': False,
}

conFalla = Queue()

def Principal(pasos):
    global fila
    imprimir_valores(fila)
    for i in range(pasos):
        fila['mc'] = valor_minimo(fila)     
        fila['paso'] = i+1   
        claves_minimo = claves_valor_minimo(fila)   
        validar_Eventos(claves_minimo)
        imprimir_valores(fila)
   

def validar_Eventos(claves_min):
    global conFalla
    global fila
    claves_a_considerar = ['clk_1', 'clk_2', 'clk_3']
    for clave in claves_min:
        if clave in claves_a_considerar:
             if fila['r'] == True:
                conFalla.put(clave)
                fila['n']= fila['n']+1
                fila[clave]= "-"     
             else:
                fila['r'] = True
                conFalla.put(clave)
                fila['n']= fila['n']+1
                fila['clk_reparacion']= fila['mc']+5
                fila[clave]= "-"
        else:
           eliminado =  conFalla.get()
           fila['n']= fila['n']-1
           fila[eliminado]=  fila['mc']+10
           if conFalla.empty():
                fila['clk_reparacion']= 0
           else:
               fila['clk_reparacion']= fila['mc']+5
               
                                
def valor_minimo(fila):
    if fila['clk_reparacion'] != 0:
        claves_a_considerar = ['clk_1', 'clk_2', 'clk_3', 'clk_reparacion']
    else:
        claves_a_considerar = ['clk_1', 'clk_2', 'clk_3'] 
    valores_a_considerar = [fila[clave] for clave in claves_a_considerar]
    valores_a_considerar = [ 9223 if valor == '-' else valor for valor in valores_a_considerar]   
    minimo = min(valores_a_considerar)
    return minimo

def claves_valor_minimo(fila):
    if fila['clk_reparacion'] != 0:
        claves_a_considerar = ['clk_1', 'clk_2', 'clk_3', 'clk_reparacion']
    else:
        claves_a_considerar = ['clk_1', 'clk_2', 'clk_3']
        
    valores_a_considerar = [fila[clave] for clave in claves_a_considerar]
    valores_a_considerar = [ 9223 if valor == '-' else valor for valor in valores_a_considerar]
    minimo = min(valores_a_considerar)
    claves_minimo = [clave for clave in claves_a_considerar if fila[clave] == minimo]
    return claves_minimo

# Ejemplo de uso:
claves_minimo = claves_valor_minimo(fila)
print("Las claves con el valor mínimo son:", claves_minimo)


def impresion_Parametros():
    print("MC: Reloj Maestro\nCLK_1: Falla en la maquina 1\nCLK_2: Falla en la maquina 2\nCLK_3: Falla en la maquina 3\nCLK_4: Tiempo en el que el server repara \nn: El numero de cola \nR: Indica si el reparador está ocupado")

def impresion_encabezados():
     print("\nPASO\tMC\tCLK_1\tCLK_2\tCLK_3\tCLK_4\tn\tR")

def imprimir_valores(diccionario):
    valores = [str(valor) for valor in diccionario.values()]
    print('\t'.join(valores))


if __name__ == "__main__":

    print("**SIMULACIÓN DE INTERRUPCIONDE MÁQUINAS**\n")
    pasos =int( input("\nIngrese el numero de pasos a imprimir:\t"))
    impresion_Parametros()
    impresion_encabezados()
    Principal(pasos)
