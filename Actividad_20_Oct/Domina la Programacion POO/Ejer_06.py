# --------------------
# Ejercicio 06
# Clase Libro con título, autor y método para mostrar info.
# --------------------
class Libro06:
    """Representa un libro con título y autor; permite mostrar información formateada."""
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def info(self):
        return f"'{self.titulo}' por {self.autor}"

# Prueba del ejercicio 06
lib = Libro06("Cien años de soledad", "Gabo")
print("E06 info:", lib.info())