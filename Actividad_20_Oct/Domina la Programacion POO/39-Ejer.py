from Ejer_06 import Libro06

# --------------------
# Ejercicio 39
# Clase Biblioteca que guarda libros (Libro06) y permite buscar por autor.
# --------------------
class Biblioteca39:
    """Biblioteca que contiene libros y puede filtrar por autor."""
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        if hasattr(libro, "titulo"):
            self.libros.append(libro)
            return True
        return False

    def buscar_por_autor(self, autor):
        return [l for l in self.libros if l.autor == autor]

# Prueba del ejercicio 39
bib = Biblioteca39()
bib.agregar_libro(Libro06("Libro A", "Autor 1"))
bib.agregar_libro(Libro06("Libro B", "Autor 2"))
print("E39 buscar Autor 1:", [l.titulo for l in bib.buscar_por_autor("Autor 1")])