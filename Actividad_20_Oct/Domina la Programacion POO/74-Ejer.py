# --------------------
# Ejercicio 74
# Clase Avion con altitud y métodos subir/bajar.
# --------------------
class Avion74:
    """Avión con altitud que puede subir o bajar."""
    def __init__(self):
        self.altitud = 0

    def subir(self, metros):
        self.altitud += metros
        return self.altitud

    def bajar(self, metros):
        self.altitud = max(0, self.altitud - metros)
        return self.altitud

# Prueba del ejercicio 74
av = Avion74()
print("E74 subir 1000:", av.subir(1000), "bajar 500:", av.bajar(500))