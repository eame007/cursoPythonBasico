import Helpers
import Database as db

def iniciar():
    while True:
        Helpers.limpiar_Pantalla()
        print("================================")
        print("Bienvenido al Gestor de Usuarios")
        print("================================")
        print("[1] Listar los clientes")
        print("[2] Buscar un cliente")
        print("[3] Agregar un cliente")
        print("[4] Modigicar un cliente")
        print("[5] Eliminar un cliente")
        print("[6] Cerrar Gestor")
        print("================================")
        
        opcion = input("> ")
        Helpers.limpiar_Pantalla()
        
        if opcion == "1":
            print("Listando los clientes...\n")
            for cliente in db.Clientes.lista:
                print(cliente)
        elif opcion == "2":
            print("Buscando los clientes...\n")
            
            dui = Helpers.leerTexto(8,8, "Los 8 digitos del DUI")
            cliente = db.Clientes.BuscarCliente(dui)
            print(cliente) if cliente else print("CLiente no encontrado")
        
        elif opcion == "3":
            print("Agregando los clientes...\n")
            dui = None  
            while True:
                dui = Helpers.leerTexto(8,8, "Los 8 digitos del DUI")
                if Helpers.validar_dui(dui, db.Clientes.lista):
                    break
            nombre = Helpers.leerTexto(3,30, "Nombre de 3 a 30 Caracteres ").capitalize()
            apellido = Helpers.leerTexto(3,30, "Apellido de 3 a 30 Caracteres ")
            db.Clientes.crearCliente(dui, nombre, apellido)
            print("Cliente agregado correctamente")
            
        elif opcion == "4":
            print("Modificando los clientes...\n")
            dui = Helpers.leerTexto(8,8, "Los 8 digitos del DUI")
            cliente = db.Clientes.BuscarCliente(dui)
            if cliente:
                nombre = Helpers.leerTexto(3,30, f"Nombre de 3 a 30 Caracteres {cliente.nombre}").capitalize()
                apellido = Helpers.leerTexto(3,30, f"Apellido de 3 a 30 Caracteres  {cliente.apellido}").capitalize()
                db.Clientes.Modificar(dui, nombre, apellido)
                print("Cliente modifiado correctamente")
            else:
                print("Cliente NO encontrado")
 
        elif opcion == "5":
            print("Eliminando los clientes...\n")
            dui = Helpers.leerTexto(8,8, "Los 8 digitos del DUI")
            print("Cliente eliminado correctamente") if db.Clientes.Eliminar(dui) else print("Cliente no encontrado")
            
        elif opcion == "6":
            print("Saliendo... Gracias y hasta luego!.\n")
            input("Presiona ENTER para salir.")
            break
        
        input("Presiona ENTER para salir")