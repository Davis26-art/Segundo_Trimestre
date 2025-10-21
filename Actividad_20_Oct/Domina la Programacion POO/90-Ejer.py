# --------------------
# Ejercicio 90
# Clase Rueda con velocidad angular (rpm).
# --------------------
class Rueda90:
    """Rueda que cambia su velocidad de rotación (rpm)."""
    def __init__(self):
        self.rpm = 0

    def acelerar(self, delta):
        self.rpm += delta
        return self.rpm

# Prueba del ejercicio 90
r90 = Rueda90()
print("E90 acelerar +100:", r90.acelerar(100))