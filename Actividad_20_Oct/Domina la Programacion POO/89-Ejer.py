# --------------------
# Ejercicio 89
# Clase Jugador con puntaje y método ganar puntos.
# --------------------
class Jugador89:
    """Jugador con puntaje acumulado."""
    def __init__(self, nombre):
        self.nombre = nombre
        self.puntaje = 0

    def ganar_puntos(self, pts):
        self.puntaje += pts
        return self.puntaje

# Prueba del ejercicio 89
j89 = Jugador89("Luis")
print("E89 puntaje:", j89.ganar_puntos(10))