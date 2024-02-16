class Libro:

    # Contructor de la clase
    def __init__(self, titulo, autor, lanzamiento, genero) -> None:
        self.titulo = titulo
        self.autor = autor
        self.lanzamiento = lanzamiento
        self.genero = genero

    def __str__(self) -> str:
        return "{} {} {} ({})".format(self.titulo, self.autor, self.genero, self.lanzamiento)


