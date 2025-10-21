# --------------------
# Ejercicio 80
# Clase Caja con volumen calculado.
# --------------------
class Caja80:
    """Caja rectangular con volumen (ancho*largo*alto)."""
    def __init__(self, ancho, largo, alto):
        self.ancho = ancho
        self.largo = largo
        self.alto = alto

    def volumen(self):
        return self.ancho * self.largo * self.alto

# Prueba del ejercicio 80
cx = Caja80(2,3,4)
print("E80 volumen:", cx.volumen())