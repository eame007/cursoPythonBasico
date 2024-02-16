 
    
from io import open
import pickle

class Catalogo:
    
    #Lista de libros
    libros = []
    
    def __init__(self):
      self.cargar()
    
    #Metodo para agregar un libro al catalog
    def agregarLibro(self, libro):
        self.libros.append(libro)
        self.guardar()
    
    #Metodo para mostrar el contenido del catalogo
    def mostrar(self):
        
        if len(self.libros) == 0:
            print("El catalogo esta vacio")
            return
        for l in self.libros:
            print(l)
    
    #Metodo para cargar el contenido
    def cargar(self):
        fichero = open("catalogo.pckl","ab+")
        fichero.seek(0)
        
        try:
            self.libros = pickle.load(fichero)
        
        except:
            print("\nEl fichero esta vacio")
        finally:
            print("Se han cargado {} libros".format(len(self.libros)))
    
   #Metodo para guardar
    def guardar(self):
        fichero = open('catalogo.pckl', 'wb')
        pickle.dump(self.libros, fichero)
        fichero.close()    
    
    
    
    
    
    
class Libro:
    
    #Contructor de la clase
    def __init__(self, titulo, autor, lanzamiento, genero) -> None:
        self.titulo = titulo
        self.autor = autor
        self.lanzamiento = lanzamiento
        self.genero = genero
        
    def __str__(self) -> str:
        return "{} {} {} ({})".format(self.titulo, self.autor, self.genero, self.lanzamiento)
    
    
    
    


# Creamos un catálogo
c = Catalogo()

c.agregarLibro(Libro("El Padrino", "Mario Puzo",1945, "Novela Negra"))

c.mostrar()

    