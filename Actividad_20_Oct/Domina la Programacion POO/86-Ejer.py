# --------------------
# Ejercicio 86
# Clase Semaforo con colores ciclando.
# --------------------
class Semaforo86:
    """Semáforo que alterna entre verde, amarillo y rojo."""
    def __init__(self):
        self.colores = ["verde", "amarillo", "rojo"]
        self.indice = 0

    def siguiente(self):
        self.indice = (self.indice + 1) % len(self.colores)
        return self.colores[self.indice]

# Prueba del ejercicio 86
s86 = Semaforo86()
print("E86 siguiente:", s86.siguiente())