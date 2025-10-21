# --------------------
# Ejercicio 77
# Clase Figura con método área (será sobreescrito).
# --------------------
class Figura77:
    """Clase base Figura con método área genérico."""
    def area(self):
        return 0

# Subclase Cuadrado
class Cuadrado77(Figura77):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2

# Prueba del ejercicio 77
sq = Cuadrado77(4)
print("E77 área cuadrado:", sq.area())