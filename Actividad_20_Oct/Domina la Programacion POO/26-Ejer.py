from Ejer_21 import Cancion21

# --------------------
# Ejercicio 26
# Clase Playlist que guarda canciones (objetos Cancion21) en lista y permite agregar.
# --------------------
class Playlist26:
    """Playlist simple que contiene objetos tipo Cancion21 (u objetos con .reproducir())."""
    def __init__(self, nombre):
        self.nombre = nombre
        self.canciones = []

    def agregar(self, cancion):
        # agrega si tiene método reproducir (duck typing simple)
        if hasattr(cancion, "reproducir"):
            self.canciones.append(cancion)
            return True
        return False

    def mostrar(self):
        return [c.titulo for c in self.canciones]

# Prueba del ejercicio 26
pl = Playlist26("Mis Favoritas")
pl.agregar(Cancion21("Song1","Artist",200))
print("E26 lista titulos:", pl.mostrar())