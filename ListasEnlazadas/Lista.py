# Clase Nodo
class Nodo:
    def __init__(self, numero) -> None:
        self.numero = numero
        self.next = None

# Clase Lista
class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def Agregar_Inicio(self, numero):
        new_nodo = Nodo(numero)
        new_nodo.next = self.head
        self.head = new_nodo

    def Agregar_Fin(self, numero):
        new_nodo = Nodo(numero)
        if self.head is None:
            self.head = new_nodo
            return
        actual = self.head
        while actual.next:
            actual = actual.next
        actual.next = new_nodo

    def Imprimir_Lista(self):
        actual = self.head
        if not actual:
            print("\nLa lista esta vacia")
            return
        while(actual):
            print(actual.numero, "->", end=" ")
            actual = actual.next
        print("\n")
   
    def Buscar_Valor(self, clave):
        actual = self.head
        while actual:
            if actual.numero == clave:
                return True
            actual = actual.next
        return False

    def Eliminar_Nodo(self, valor):
        actual = self.head
        anterior = None
        if not actual:
            print("\nLa lista está vacía")
            return
        if self.Buscar_Valor(valor):
            if actual.numero == valor:
                self.head = actual.next
                return
            while actual:
                if actual.numero == valor:
                    anterior.next = actual.next
                    print("Nodo eliminado")
                    return
                anterior = actual
                actual = actual.next
        print("\nEl valor no existe en la lista")
        return

    def Guardar_Lista(self, nombre_archivo):
        actual = self.head
        with open(nombre_archivo, 'w') as file:
            while actual:
                file.write(str(actual.numero) + '\n')
                actual = actual.next
        print("Lista guardada en el archivo", nombre_archivo)

# Clase principal
class Main:
    def __init__(self):
        self.lista = LinkedList()

    def menu(self):
        while True:
            print("\n[1] Crear Lista enlazada")
            print("[2] Agregar nodo al inicio")
            print("[3] Agregar nodo al final")
            print("[4] Eliminar nodo")
            print("[5] Buscar valor")
            print("[6] Imprimir lista")
            print("[7] Guardar lista en archivo")
            print("[8] Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                # Crear Lista enlazada
                self.lista = LinkedList()
                print("Lista creada")
            elif opcion == '2':
                # Agregar nodo al inicio
                numero = input("Ingrese el número para el nodo: ")
                self.lista.Agregar_Inicio(numero)
                print("Nodo agregado al inicio")
            elif opcion == '3':
                # Agregar nodo al final
                numero = input("Ingrese el número para el nodo: ")
                self.lista.Agregar_Fin(numero)
                print("Nodo agregado al final")
            elif opcion == '4':
                # Eliminar nodo
                valor = input("Ingrese el valor del nodo a eliminar: ")
                self.lista.Eliminar_Nodo(valor)
                
            elif opcion == '5':
                # Buscar valor
                valor = input("Ingrese el valor a buscar: ")
                if self.lista.Buscar_Valor(valor):
                    print("El valor está en la lista")
                else:
                    print("El valor no está en la lista")
            elif opcion == '6':
                # Imprimir lista
                self.lista.Imprimir_Lista()
            elif opcion == '7':
                # Guardar lista en archivo
                nombre_archivo = input("Ingrese el nombre del archivo para guardar la lista: ")
                self.lista.Guardar_Lista(nombre_archivo)
            elif opcion == '8':
                # Salir
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    main = Main()
    main.menu()
