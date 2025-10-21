# --------------------
# Ejercicio 21
# Clase Cancion con título, artista y duración; método reproducir (simulado).
# --------------------
class Cancion21:
    """Canción con metadatos y método para mostrar 'reproduciendo'."""
    def __init__(self, titulo, artista, duracion_seg):
        self.titulo = titulo
        self.artista = artista
        self.duracion = int(duracion_seg)

    def reproducir(self):
        # Simulación: solo devuelve un string con el título y artista
        return f"Reproduciendo '{self.titulo}' de {self.artista} ({self.duracion}s)"

# Prueba del ejercicio 21
canc = Cancion21("Imagine", "John Lennon", 183)
print("E21:", canc.reproducir())