class Nodo:
    def __init__(self, numero) -> None:
        self.numero = numero
        self.next = None



class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def Agregar_Inicio(self, numero):
        new_nodo = Nodo(numero)
        if(self.head is None):
            self.head = new_nodo
            return
        new_nodo.next = self.head
        self.head = new_nodo

    def Agregar_fin(self, numero):
        new_nodo = Nodo(numero)
        actual = self.head
        while(actual.next is not None):
            actual = actual.next
        actual.next = new_nodo

    def printLista(self):
        actual = self.head

        if( actual is None):
            print("\nLa lista esta vacia")
            return
        while(actual):
            print(actual.numero, "->", end=" ")
            actual = actual.next
        print("\n")
   
    def buscarValor(self, clave):
        actual = self.head
        if( actual is None):
            print("\nLa lista esta vacia")
            return
        while(actual):
            if actual.numero == clave:
                return True
            else:
                actual = actual.next
        return False
    
    def Eliminar_Nodo(self, valor):
        actual = self.head
        anterior = None
        if( actual is None):
            print("\nLa lista esta vacia")
            return
        while(actual):
            if actual.numero == valor :
                anterior.next = actual.next
                return
            else:
                anterior = actual
                actual = actual.next
            

mi_lista = LinkedList()
mi_lista.Agregar_Inicio(5)
mi_lista.Agregar_Inicio(7)
mi_lista.Agregar_Inicio(8)
mi_lista.Agregar_fin(20)
mi_lista.printLista()
mi_lista.Eliminar_Nodo(7)
mi_lista.printLista()
print("\nValor encontrado ") if mi_lista.buscarValor(34) else print("\nValor no encontrado")
print("\nValor encontrado ") if mi_lista.buscarValor(5) else print("\nValor no encontrado")