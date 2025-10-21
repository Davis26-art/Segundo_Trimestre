import random

# --------------------
# Ejercicio 53
# Clase JuegoMoneda con método lanzar que devuelve 'cara' o 'cruz'.
# --------------------
class JuegoMoneda53:
    """Juego simple: lanzar moneda y obtener cara o cruz."""
    def lanzar(self):
        return random.choice(["cara", "cruz"])

# Prueba del ejercicio 53
mon = JuegoMoneda53()
print("E53 resultado:", mon.lanzar())