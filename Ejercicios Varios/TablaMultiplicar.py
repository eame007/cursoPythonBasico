from io import open

def escribirTabla(numero):
    nombre = "Tabla-"+str(numero)+".txt"    
    fichero = open(nombre, "w")
    for i in range(1,13):
        elemento = "{} x {} = {}".format(numero, i, (i*numero))
        fichero.write(elemento+"\n")  

def imprimirTabla():
    pass

while True:
    try:
        numero = int(input("\nIngrese el numero del que desea escribir la tabla: "))
        escribirTabla(numero)
    except:
        print("\n El valor ingresado no es un numero correcto")
    finally:
        print("\Archivo escrito y guardado")
        imprimirTabla()
        break
    

