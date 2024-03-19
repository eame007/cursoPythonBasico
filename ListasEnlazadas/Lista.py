class  Nodo:
    def __init__(self, numero) :
        self.numero = numero
        self.next = None
        
        
class LinkedList:
    def __init__(self) :
         self.head = None
            
    def insert_node_start(self, numero):
            nodo = Nodo(numero)
            if(self.head is None):
                self.head = nodo
                return
            
            nodo.next = self.head
            self.head = nodo
        
    def insert_node_end(self, numero):
            nodo = Nodo(numero)
            if(self.head is None):
                self.head = nodo
                return
            
            actual = self.head
            while(actual.next is not None):
                actual = actual.next
            actual.next = nodo
            
    def longitudLista(self):
            valor = 0
            actual = self.head
            while(actual.next is not None):
                valor +=1
                actual = actual.next
            return valor
                
             
    def estaVacia(self):
            True if self.head is None else False
            
    def printList(self):
            actual = self.head
            if self.estaVacia:
                print("La lista esta vacia\n")
            elif self.longitudLista == 1:
                print(actual.numero)
            else:
                 while(actual.next is not None):
                     print(actual.numero, "->", end=" ")
                     actual = actual.next
                     
                     
mi_lista = LinkedList()
print(mi_lista.estaVacia)
print(mi_lista.longitudLista)
mi_lista.insert_node_start(25)
mi_lista.insert_node_start(5)
mi_lista.insert_node_end(3)
print(mi_lista.estaVacia)
print(mi_lista.longitudLista)
mi_lista.printList()

                     
                     
    