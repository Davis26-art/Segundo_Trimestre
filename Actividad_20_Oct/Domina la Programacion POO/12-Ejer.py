# --------------------
# Ejercicio 12
# Clase Punto2D con coordenadas x,y y método distancia al origen.
# --------------------
class Punto12:
    """Punto en 2D con calculo de distancia al origen (0,0)."""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distancia_origen(self):
        return (self.x**2 + self.y**2)**0.5

# Prueba del ejercicio 12
p = Punto12(3,4)
print("E12 distancia_origen:", p.distancia_origen())  # 5.0